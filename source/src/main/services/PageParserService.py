from abc import ABC, abstractmethod
from bs4 import BeautifulSoup, NavigableString, Tag
import re

"""Сервис для парсинга данных"""


class PageParserServiceInterface(ABC):
    @abstractmethod
    def getContent(self, target):
        pass

""" В данной реализации постараемся реализовать универсальный парсер. 
    Для этого будем выбирать контент только из указанных в __targetTags тегов.
    Обход по элементам будет происходить в рекурсии- 
    т.к. мы заранее не знаем, что нам нужно и где оно лежит."""
class DefaultBsPageParserService(PageParserServiceInterface):
    def __init__(self):
        self.__targetTags = [
            "h1", "h2", "h3", "h4", "h5", "h6", 
            "p", "span"
            ]
        self.__linkPattern = "[{link}]"
        super().__init__()

    def getContent(self, target):
        soup = BeautifulSoup(target, "html.parser")
        body = soup.body
        result = []
        self.__recursionRun(result, body)
        return result

    def __recursionRun(self, result: list, element):
        if isinstance(element, Tag):
            if element.name in self.__targetTags:
                tagContent = self.__getTagContent(element)
                if tagContent:
                    result.append(tagContent)
            else:
                for child in element:
                    self.__recursionRun(result, child)
        return result

    def __getTagContent(self, element):
        result = None
        contents = element.contents
        textContent = ""
        if (len(contents) > 0 and isinstance(contents[0], NavigableString)):
            for content in contents:
                #Если content это строка и в ней есть хотя бы одна буква- берём.
                if isinstance(content, NavigableString) and re.match("^.*[a-zA-Zа-яёА-ЯЁ]+.*$", content):
                    textContent += content.replace("\n", "").replace("\r", "")
                #Частный случай для тега a- нам нужно взять и текст и ссылку(обрамив её квадратными скобками)
                elif isinstance(content, Tag) and content.name == "a":
                    textContent += content.text + self.__linkPattern.format(link=content.get("href", ""))
        else:
            textContent = element.text
        result = textContent
        return result

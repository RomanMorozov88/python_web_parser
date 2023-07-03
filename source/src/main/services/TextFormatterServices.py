from abc import ABC, abstractmethod
import textwrap

"""Сервис для создания итогового текста"""


class TextFormatterServiceInterface(ABC):
    @abstractmethod
    def getReadyText(self, textArray):
        pass


class DefaultTextFormatterService(TextFormatterServiceInterface):
    def __init__(self, stringLength):
        self.__stringLength: int = stringLength
        self.__mainPattern = "\n{content}\n"

    def getReadyText(self, contentList):
        result = ""
        for line in contentList:
            text = self.__getFormattedText(line.strip())
            result += text
        return result
    
    def __getFormattedText(self, rawText):
        result = textwrap.fill(rawText, width=int(self.__stringLength))
        return self.__mainPattern.format(content = result)

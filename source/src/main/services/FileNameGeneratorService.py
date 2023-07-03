import re

"""Создание имени файла на основе указанной ссылки"""


def generateFileNameByLink(link: str):
    buffer = re.sub("https?://", "", link)
    buffer = re.sub("(\/|.[a-zA-Z]+)$", ".txt", buffer)
    return buffer

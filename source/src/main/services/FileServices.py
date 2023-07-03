from abc import ABC, abstractmethod
import pathlib


"""Сервис для записи в фаил"""


class FileServiceInterface(ABC):
    @abstractmethod
    def writeInFile(self, directory, fileName, text):
        pass


class DefaultFileService(FileServiceInterface):
    def writeInFile(self, directory, fileName, text):
        resultFile = pathlib.Path(directory + fileName)
        resultFile.parent.mkdir(exist_ok=True, parents=True)
        resultFile.write_text(text, encoding="utf-8")
        return resultFile.name

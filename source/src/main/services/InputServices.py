from abc import ABC, abstractmethod

"""Сервис для ввода данных"""


class InputServiceInterface(ABC):
    @abstractmethod
    def getInputData(self):
        pass


class ConsoleInputService(InputServiceInterface):
    def getInputData(self):
        return str(input())

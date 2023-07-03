from abc import ABC, abstractmethod
import requests
import logging

from models.Models import ResponseModel


"""Сервис для загрузки данных с сайта по указанной ссылке"""


class LoadPageServiceInterface(ABC):
    @abstractmethod
    def loadPageContent(self, link) -> ResponseModel:
        pass


class RequestLoadPageService(LoadPageServiceInterface):
    def loadPageContent(self, link):
        result = ResponseModel()
        try:
            response = requests.get(link)
            result.code = response.status_code
            if result.code == 200:
                result.text = response.text
            return result
        except Exception as e:
            logging.exception(e)

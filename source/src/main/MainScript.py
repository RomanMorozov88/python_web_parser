import configparser
import re
from services.LoadPageServices import RequestLoadPageService
from services.FileNameGeneratorService import generateFileNameByLink
from services.InputServices import ConsoleInputService
from services.PageParserService import DefaultBsPageParserService
from services.TextFormatterServices import DefaultTextFormatterService
from services.FileServices import DefaultFileService
import sys


def main():

    urlRegex = "(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})?"

    config = configparser.ConfigParser()
    config.read("settings.ini")
    dirPath = config["general"].get("dir", "./")
    stringLength = config["general"].get("string_length", 80)

    inputService = ConsoleInputService()
    loadPageService = RequestLoadPageService()
    textFormatterService = DefaultTextFormatterService(stringLength)
    fileService = DefaultFileService()

    pageParserService = DefaultBsPageParserService()

    if len(sys.argv) == 2:
        link = sys.argv[1]
    else:
        print("Введите ссылку для обработки:")
        link = inputService.getInputData()
    while True:
        if(re.match(urlRegex, link)):
            break
        else:
            print("Некорректная ссылка. Попробуйте ещё раз:")
            link = inputService.getInputData()

    print(">>>>>>>>>>>>>>>>>>>> _START_")

    response = loadPageService.loadPageContent(link)
    if response and response.code == 200:
        fileName = generateFileNameByLink(link)
        contentList = pageParserService.getContent(response.text)
        text = textFormatterService.getReadyText(contentList)
        fullFileName = fileService.writeInFile(dirPath, fileName, text)
        print("Данные записаны в фаил:" + fullFileName)
    elif response and response.code:
        print("Код ответа на запрос по ссылке: " +
              str(response.code))

    print(">>>>>>>>>>>>>>>>>>>> _FINISH_")

    print("Нажмите Enter для завершения программы:")
    inputService.getInputData()


if __name__ == "__main__":
    main()

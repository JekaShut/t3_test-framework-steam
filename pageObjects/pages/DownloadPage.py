from logger.logger import Logger
from utils import ButtonOperations, Wait
from framework.BaseElement import TimeoutException, NoSuchElementException

logger = Logger(logger="DownloadPage").getlog()


class DownloadPage:
    def __init__(self):
        self.downloadButtonClass = "about_install"
        self.waitTime = 10

    def clickButtonToDownload(self):
        logger.info("Waiting for the DOM to load the class")
        try:
            Wait.WaitClass(self.downloadButtonClass, self.waitTime)
        except TimeoutException:
            logger.error("Cannot find element! " + self.downloadButtonClass)
        logger.info("Trying to click button with class: " + self.downloadButtonClass)
        ButtonOperations.ClickButtonClass(self.downloadButtonClass)

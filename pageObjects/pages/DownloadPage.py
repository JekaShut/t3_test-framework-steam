from framework.BaseElement import *
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations
from logger.logger import Logger

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

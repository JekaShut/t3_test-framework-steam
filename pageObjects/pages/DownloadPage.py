from framework import BaseElement
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations
from logger.logger import Logger

logger = Logger(logger="DownloadPage").getlog()

class DownloadPage:
    def __init__(self):
        self.downloadButtonClass = "about_install"
        self.waitTime = 10

    def clickButtonToDownload(self):
        logger.info("Waiting for the DOM to load the class")
        Wait.WaitClass(self.downloadButtonClass, self.waitTime)
        logger.info("Trying to click button with class: " + self.downloadButtonClass)
        ButtonOperations.ClickButtonClass(self.downloadButtonClass)

from framework import framework
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ManyItems


class DownloadPage:
    def __init__(self):
        self.downloadButtonClass = "about_install"
        self.waitTime = 10

    def clickButtonToDownload(self):
        Wait.WaitClass(self.downloadButtonClass, self.waitTime)
        ButtonOperations.ClickButtonClass(self.downloadButtonClass)
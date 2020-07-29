from framework import BaseElement
from common import jsonGetter
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations
import time
from pageObjects.pages import DownloadPage, MainPage
from pageObjects.SystemAsserts import fileIsDownloaded




class TestSteamDownload:

    def test_steampageload(self):
        MainPage.MainPage().clickButtonToDownload()
        DownloadPage.DownloadPage().clickButtonToDownload()

    def test_fileIsDownloaded(self):
        assert fileIsDownloaded.fileIsDownloaded().checkFile() == True




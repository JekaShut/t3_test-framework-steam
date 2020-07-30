from framework import BaseElement
from common import jsonGetter
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations
import time
from pageObjects.pages import DownloadPage, MainPage
from pageObjects.SystemAsserts import fileIsDownloaded
from utils import GetUrl
from logger.logger import Logger

logger = Logger(logger="TC-1").getlog()

SITE = jsonGetter.GetJson.getConfig("SITE")


class TestSteamDownload:

    def test_steampageload(self):
        LinkOperations.OpenLink(SITE)
        assert SITE == GetUrl.Get().CurrentUrl()
        MainPage.MainPage().clickButtonToDownload()
        DownloadPage.DownloadPage().clickButtonToDownload()

    def test_fileIsDownloaded(self):
        assert fileIsDownloaded.fileIsDownloaded().checkFile() == True




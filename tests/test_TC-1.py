from common import jsonGetter
from logger.logger import Logger
from pageObjects.SystemAsserts import fileIsDownloaded
from pageObjects.pages import DownloadPage, MainPage
from utils import GetUrl, StopBrowser
from utils import LinkOperations
import time
logger = Logger(logger="TC-1").getlog()

SITE = jsonGetter.GetJson.getConfig("SITE")


class TestSteamDownload:

    def test_steampageload(self):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.OpenLink(SITE)
        assert SITE == GetUrl.Get().CurrentUrl()
        MainPage.MainPage().clickButtonToDownload()
        DownloadPage.DownloadPage().clickButtonToDownload()

    def test_fileIsDownloaded(self):
        assert fileIsDownloaded.fileIsDownloaded().checkFile() == True

    def test_TearDown(self):
        time.sleep(2)
        logger.info("Trying to stop browser")
        StopBrowser.stop()


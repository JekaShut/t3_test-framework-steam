from framework import BaseElement
from common import jsonGetter
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations
import time
from pageObjects.pages import DownloadPage, MainPage
from pageObjects.SystemAsserts import fileIsDownloaded
from logger.logger import Logger

LOCAL = jsonGetter.GetJson.get("LOCAL")
SITE = jsonGetter.GetJson.get("SITE")
actualBrowser = jsonGetter.GetJson.get("actualBrowser")

logger = Logger(logger="BaseTest").getlog()


class TestRunbrowser():
    def test_runbrowser(self):
        BaseElement.RunBrowser(actualBrowser)
        LinkOperations.OpenLink(SITE)
        logger.info("Test")

    def test_lang(self):
        MainPage.MainPage().setLang()





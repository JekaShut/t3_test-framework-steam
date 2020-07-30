from framework import BaseElement
from common import jsonGetter
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, GetUrl, GetText
import time
from pageObjects.pages import DownloadPage, MainPage
from pageObjects.SystemAsserts import fileIsDownloaded
from logger.logger import Logger

logger = Logger(logger="BaseTest").getlog()

LOCAL = jsonGetter.GetJson.getConfig("LOCAL")
SITE = jsonGetter.GetJson.getConfig("SITE")
actualBrowser = jsonGetter.GetJson.getConfig("actualBrowser")
ruLang = jsonGetter.GetJson.getData("ruLang")
enLang = jsonGetter.GetJson.getData("enLang")




logger.info("\n" + "Browser : " + actualBrowser + "\n" + "Language is: " + LOCAL)


class TestRunbrowser():
    def test_runbrowser(self):
        #BaseElement.RunBrowser(actualBrowser)
        logger.info("Trying to open url: " + SITE)
        LinkOperations.OpenLink(SITE)


    def test_lang(self):
        assert SITE == GetUrl.Get().CurrentUrl()
        logger.info("Trying to set language")
        MainPage.MainPage().setLang()
        language = GetText.GetText().byXpath(MainPage.MainPage().DropDownXpath)






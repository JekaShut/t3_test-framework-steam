from framework import BaseElement
from common import jsonGetter
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, MouseOperations
import time
from pageObjects.pages import DownloadPage, MainPage, ActionPage
from pageObjects.SystemAsserts import fileIsDownloaded

from framework.BaseElement import *
from selenium.webdriver.common.action_chains import ActionChains

LOCAL = jsonGetter.GetJson.get("LOCAL")
SITE = jsonGetter.GetJson.get("SITE")
actualBrowser = jsonGetter.GetJson.get("actualBrowser")


class TestRunbrowser():
    def test_runbrowser(self):
        BaseElement.RunBrowser(actualBrowser)
        LinkOperations.OpenLink(SITE)

    #def test_lang(self):
        #MainPage.MainPage().setLang()


class TestDiscountCalc:
    def test_ClickAction(self):
        MainPage.MainPage().moveMouseToMenu()
        MainPage.MainPage().clickAction()
        ActionPage.ActionPage().navigateToTopSelling()
        ActionPage.ActionPage().findHigestDiscount()









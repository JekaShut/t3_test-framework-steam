from framework import BaseElement
from common import jsonGetter
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, MouseOperations
import time
from pageObjects.pages import DownloadPage, MainPage, ActionPage, GamePage
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
        gamesData = ActionPage.ActionPage().findLowestDiscount()
        gameData = GamePage.GamePage().getPrices()
        assert gamesData[0] == gameData[0], "Prices are not equal"
        assert gamesData[1] == gameData[1], "Prices are not equal"
        assert gamesData[2] + " USD" == gameData[2], "Prices are not equal"










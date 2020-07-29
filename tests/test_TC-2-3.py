from framework import BaseElement
from common import jsonGetter
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, MouseOperations
import time
from pageObjects.pages import DownloadPage, MainPage, GameTypePage, GamePage
from pageObjects.SystemAsserts import fileIsDownloaded

from framework.BaseElement import *
from selenium.webdriver.common.action_chains import ActionChains

LOCAL = jsonGetter.GetJson.get("LOCAL")
SITE = jsonGetter.GetJson.get("SITE")
actualBrowser = jsonGetter.GetJson.get("actualBrowser")


class TestRunbrowser():
    def test_runbrowser(self):
        BaseElement.RunBrowser(actualBrowser)


    #def test_lang(self):
        #MainPage.MainPage().setLang()


class TestC_2:
    def test_discountCalcHight(self):
        LinkOperations.OpenLink(SITE)
        MainPage.MainPage().moveMouseToMenu()
        MainPage.MainPage().clickAction()
        GameTypePage.ActionPage().navigateToTopSelling()
        gamesData = GameTypePage.ActionPage().findHigestDiscount()
        gameData = GamePage.GamePage().getPrices()
        assert gamesData[0] == gameData[0], "Prices are not equal"
        assert gamesData[1] == gameData[1], "Prices are not equal"
        assert gamesData[2] + " USD" == gameData[2], "Prices are not equal"

class TestC_3:
    def test_discountCalcLow(self):
        LinkOperations.OpenLink(SITE)
        MainPage.MainPage().moveMouseToMenu()
        MainPage.MainPage().clickIndie()
        GameTypePage.ActionPage().navigateToTopSelling()
        gamesData = GameTypePage.ActionPage().findLowestDiscount()
        gameData = GamePage.GamePage().getPrices()
        assert gamesData[0] == gameData[0], "Prices are not equal"
        assert gamesData[1] == gameData[1], "Prices are not equal"
        assert gamesData[2] + " USD" == gameData[2], "Prices are not equal"








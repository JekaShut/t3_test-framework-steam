from framework import BaseElement
from common import jsonGetter
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, MouseOperations , GetUrl, GetText
import time
from pageObjects.pages import DownloadPage, MainPage, GameTypePage, GamePage
from pageObjects.SystemAsserts import fileIsDownloaded

from framework.BaseElement import *
from selenium.webdriver.common.action_chains import ActionChains
from logger.logger import Logger

logger = Logger(logger="TC-2").getlog()

LOCAL = jsonGetter.GetJson.getConfig("LOCAL")
SITE = jsonGetter.GetJson.getConfig("SITE")
actualBrowser = jsonGetter.GetJson.getConfig("actualBrowser")
actionTitleRu = jsonGetter.GetJson.getData("ruActionTitle")
actionTitleEn = jsonGetter.GetJson.getData("enActionTitle")
indieTitleRu = jsonGetter.GetJson.getData("ruIndieTitle")
indieTitleEn = jsonGetter.GetJson.getData("enIndieTitle")

class TestRunbrowser():
    def test_runbrowser(self):
        BaseElement.RunBrowser(actualBrowser)


    #def test_lang(self):
        #MainPage.MainPage().setLang()


class TestC_2:
    def test_discountCalcHight(self):
        LinkOperations.OpenLink(SITE)
        assert SITE == GetUrl.Get().CurrentUrl()
        MainPage.MainPage().moveMouseToMenu()
        MainPage.MainPage().clickAction()
        TITLE = GetText.GetText().byXpath(GameTypePage.ActionPage().TitleXpath)
        if LOCAL == "ru":
            assert TITLE == actionTitleRu
        if LOCAL == "en":
            assert TITLE == actionTitleEn
        GameTypePage.ActionPage().navigateToTopSelling()
        gamesData = GameTypePage.ActionPage().findHighestDiscount()
        gameData = GamePage.GamePage().getPrices()
        assert gamesData[3] == gameData[3], "App name not equal"
        assert gamesData[0] == gameData[0], "Prices are not equal"
        assert gamesData[1] == gameData[1], "Prices are not equal"
        assert gamesData[2] + " USD" == gameData[2], "Prices are not equal"

class TestC_3:
    def test_discountCalcLow(self):
        LinkOperations.OpenLink(SITE)
        MainPage.MainPage().moveMouseToMenu() # FireFoxBUG idk
        MainPage.MainPage().clickIndie()
        TITLE = GetText.GetText().byXpath(GameTypePage.ActionPage().TitleXpath)
        if LOCAL == "ru":
            assert TITLE == indieTitleRu
        if LOCAL == "en":
            assert TITLE == indieTitleEn
        GameTypePage.ActionPage().navigateToTopSelling()
        gamesData = GameTypePage.ActionPage().findLowestDiscount()
        gameData = GamePage.GamePage().getPrices()
        assert gamesData[0] == gameData[0], "Prices are not equal"
        assert gamesData[1] == gameData[1], "Prices are not equal"
        assert gamesData[2] + " USD" == gameData[2], "Prices are not equal"








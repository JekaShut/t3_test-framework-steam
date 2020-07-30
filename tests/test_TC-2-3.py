from framework import BaseElement
from framework.BaseElement import *
from logger.logger import Logger
from pageObjects.pages import MainPage, GameTypePage, GamePage
from utils import LinkOperations, GetUrl, \
    GetText

logger = Logger(logger="TC-2").getlog()

LOCAL = jsonGetter.GetJson.getConfig("LOCAL")
SITE = jsonGetter.GetJson.getConfig("SITE")
actualBrowser = jsonGetter.GetJson.getConfig("actualBrowser")
actionTitleRu = jsonGetter.GetJson.getData("ruActionTitle")
actionTitleEn = jsonGetter.GetJson.getData("enActionTitle")
indieTitleRu = jsonGetter.GetJson.getData("ruIndieTitle")
indieTitleEn = jsonGetter.GetJson.getData("enIndieTitle")
ru = jsonGetter.GetJson.getData("ru")
en = jsonGetter.GetJson.getData("en")


class TestRunbrowser():
    def test_runbrowser(self):
        BaseElement.RunBrowser(actualBrowser)

    # def test_lang(self):
    # MainPage.MainPage().setLang()


class TestC_2:
    def test_discountCalcHight(self):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.OpenLink(SITE)
        assert SITE == GetUrl.Get().CurrentUrl()
        MainPage.MainPage().moveMouseToMenu()
        MainPage.MainPage().clickAction()
        TITLE = GetText.GetText().byXpath(GameTypePage.ActionPage().TitleXpath)
        if LOCAL == ru:
            assert TITLE == actionTitleRu
        if LOCAL == en:
            assert TITLE == actionTitleEn
        GameTypePage.ActionPage().navigateToTopSelling()
        gamesData = GameTypePage.ActionPage().findHighestDiscount()
        ####
        # /тут должна быть проверка проверки возраста / #
        GamePage.GamePage().checkRatedContent()
        ###
        gameData = GamePage.GamePage().getPrices()
        assert gamesData[3] == gameData[3], "App name not equal"
        assert gamesData[0] == gameData[0], "Prices are not equal"
        assert gamesData[1] == gameData[1], "Prices are not equal"
        assert gamesData[2] + " USD" == gameData[2], "Prices are not equal"


class TestC_3:
    def test_discountCalcLow(self):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.OpenLink(SITE)
        assert SITE == GetUrl.Get().CurrentUrl()
        MainPage.MainPage().moveMouseToMenu()  # FireFoxBUG idk
        MainPage.MainPage().clickIndie()
        TITLE = GetText.GetText().byXpath(GameTypePage.ActionPage().TitleXpath)
        if LOCAL == "ru":
            assert TITLE == indieTitleRu
        if LOCAL == "en":
            assert TITLE == indieTitleEn
        GameTypePage.ActionPage().navigateToTopSelling()
        gamesData = GameTypePage.ActionPage().findLowestDiscount()
        ####
        # /тут должна быть проверка проверки возраста / #
        GamePage.GamePage().checkRatedContent()
        ###
        gameData = GamePage.GamePage().getPrices()
        assert gamesData[3] == gameData[3], "App name not equal"
        assert gamesData[0] == gameData[0], "Prices are not equal"
        assert gamesData[1] == gameData[1], "Prices are not equal"
        assert gamesData[2] + " USD" == gameData[2], "Prices are not equal"

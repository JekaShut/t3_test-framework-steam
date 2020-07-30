from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, GetText, MouseOperations
from common import jsonGetter
import time
from pageObjects.pages.Logic import  ActionPageLogic
from framework.BaseElement import *
from logger.logger import Logger

logger = Logger(logger="GamePage").getlog()

class GamePage:
    def __init__(self):
        self.WaitTime = 10
        self.discountPriceOnPageXpath = "//div[@class='game_area_purchase_game_wrapper']/div/div/div/div/div/div[@class='discount_final_price']"
        self.PriceOnPageXpath = "//div[@class='game_area_purchase_game_wrapper']/div/div/div/div/div/div[@class='discount_original_price']"
        self.DiscountXpath = "//div[@class='game_area_purchase_game_wrapper']/div/div/div/div/div[@class='discount_pct']"
        self.GameName = "//div[@class='apphub_AppName']"
        self.RatedContentText = "//*[@id='app_agegate']/div/div[@class='agegate_text_container']/h2"
        self.RatedYearSelect = "//*[@id='ageYear']"
        self.RatedYearOption = "//*[@id='ageYear']/option[@value='2001']"
        self.RatedConfirmButton = "//*[@id='app_agegate']/div/div[@class='agegate_text_container btns']/a"

    def getPrices(self):
        logger.info("Waiting for the DOM to load the class")
        try:
            Wait.WaitXpath(self.DiscountXpath, self.WaitTime)
        except TimeoutException:
            logger.error("Cannot find element! " + self.DiscountXpath)
        try:
            gamePageDiscount = ElementOperations.findOneElement.byXpath(self, self.DiscountXpath).text
            gamePagePrice = ElementOperations.findOneElement.byXpath(self, self.PriceOnPageXpath).text
            gamePageDiscountPrice = ElementOperations.findOneElement.byXpath(self, self.discountPriceOnPageXpath).text
            gamePageName = ElementOperations.findOneElement.byXpath(self, self.GameName).text
        except NoSuchElementException:
            logger.error("Cannot find one of elements!")
        gameData = [gamePageDiscount, gamePagePrice, gamePageDiscountPrice, gamePageName]
        logger.info("Getting element data from the page: " + ", ".join(gameData))
        return(gameData)

    def checkRatedContent(self):
        try:
            logger.info("Found rated banner. Trying to resolve it")
            try:
                Wait.WaitXpath(self.RatedContentText, self.WaitTime)
            except TimeoutException:
                logger.error("Cannot found element: " + self.RatedContentText)
            # bannertext = GetText.GetText().byXpath(self.RatedContentText)
            Wait.WaitXpath(self.RatedYearSelect, self.RatedContentText)
            ButtonOperations.ClickButtonXpath(self.RatedYearSelect)
            ButtonOperations.ClickButtonXpath(self.RatedYearOption)
            ButtonOperations.ClickButtonXpath(self.RatedConfirmButton)


        except NoSuchElementException:
            logger.info("No rated content banner found. Keeping forward")
            pass


from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, GetText, MouseOperations
from common import jsonGetter
import time
from pageObjects.pages.Logic import  ActionPageLogic
from framework.BaseElement import *
from logger.logger import Logger

logger = Logger(logger="GameTypePage").getlog()

class ActionPage:
    def __init__(self):
        self.WaitTime = 10
        self.actionTitleXpath = "//h2[@class='pageheader']"
        self.TitleXpath = "//h2[@class='pageheader']"
        self.topSellXpath = "//*[@id='tab_select_TopSellers']/div"
        self.pageXpath = "//*[@id='TopSellers_links']/span[2]"
        self.gamesXpath = "//*[@id='TopSellersRows']/a"
        self.discountClass = "discount_pct"
        self.topSellRowXpath = "//*[@id='TopSellersRows']"
        self.discountXpath = "a/div/div[@class='discount_pct']"
        self.originalPriceXpath = "../div/div[@class='discount_original_price']"
        self.discountPriceXpath = "../div/div[@class='discount_final_price']"
        self.GameName = "../../div/div[@class='tab_item_name']"
        self.lastGameXpath = "//*[@id='NewReleasesRows']/a[15]"




    def navigateToTopSelling(self):
        logger.info("Waiting for the DOM to load the class")
        try:
            Wait.WaitXpath(self.actionTitleXpath, self.WaitTime)
        except TimeoutException:
            logger.error("Cannot find element! " + self.actionTitleXpath)
        logger.info("Trying to click element: " + self.topSellXpath)
        ButtonOperations.ClickButtonXpath(self.topSellXpath)


    def findLowestDiscount(self):
        logger.info("Waiting for the DOM to load the class")
        try:
            Wait.WaitXpath(self.topSellRowXpath, self.WaitTime)
        except TimeoutException:
            logger.error("Cannot find element! " + self.topSellRowXpath)
        topSellRow = ElementOperations.findOneElement.byXpath(self, self.topSellRowXpath)
        discountElems = ElementOperations.findManyElements.byXpath(self, self.discountXpath, topSellRow)
        logger.info("Trying to sort elements from low to hight")
        sortedDisc = ActionPageLogic.SortDiscountElems().get(discountElems)
        try:
            gamesPageDiscount = sortedDisc[0][1]                                                                                            # %
        except:
            logger.error("No games with any discount")
        gamesPagePrice = ElementOperations.findOneElement.byXpath(self, self.originalPriceXpath, sortedDisc[0][0]).text                 # WithoutDiscount
        gamesPageDiscountPrice = ElementOperations.findOneElement.byXpath(self, self.discountPriceXpath, sortedDisc[0][0]).text         # WithDiscount
        gameName = ElementOperations.findOneElement.byXpath(self, self.GameName, sortedDisc[0][0]).text
        data = [gamesPageDiscount, gamesPagePrice, gamesPageDiscountPrice, gameName]
        logger.info("Getting data: " + ", ".join(data))
        logger.info("Trying to click game button with lowest discount")
        sortedDisc[0][0].click()

        return(data)

    def findHighestDiscount(self):
        logger.info("Waiting for the DOM to load the class")
        Wait.WaitXpath(self.topSellRowXpath, self.WaitTime)
        topSellRow = ElementOperations.findOneElement.byXpath(self, self.topSellRowXpath)
        discountElems = ElementOperations.findManyElements.byXpath(self, self.discountXpath, topSellRow)
        logger.info("Trying to sort elements from low to hight")
        sortedDisc = ActionPageLogic.SortDiscountElems().get(discountElems)
        try:
            gamesPageDiscount = sortedDisc[-1][1]                                                                                            # %
        except:
            logger.error("No games with any discount")
        gamesPagePrice = ElementOperations.findOneElement.byXpath(self, self.originalPriceXpath, sortedDisc[-1][0]).text                 # WithoutDiscount
        gamesPageDiscountPrice = ElementOperations.findOneElement.byXpath(self, self.discountPriceXpath, sortedDisc[-1][0]).text         # WithDiscount
        gameName = ElementOperations.findOneElement.byXpath(self, self.GameName, sortedDisc[0][0]).text
        data = [gamesPageDiscount, gamesPagePrice, gamesPageDiscountPrice, gameName]
        logger.info("Getting data: " + ", ".join(data))
        logger.info("Trying to click game button with highest discount")
        sortedDisc[-1][0].click()
        return(data)
        #ADD RATED CONTENT BANNER




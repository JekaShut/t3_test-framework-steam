from framework import BaseElement
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, GetText, MouseOperations
from common import jsonGetter
import time
from pageObjects.pages.Logic import  ActionPageLogic
from framework.BaseElement import *

class ActionPage:
    def __init__(self):
        self.WaitTime = 10
        self.actionTitleXpath = "//h2[@class='pageheader']"
        self.topSellXpath = "//*[@id='tab_select_TopSellers']/div"
        self.pageXpath = "//*[@id='TopSellers_links']/span[2]"
        self.gamesXpath = "//*[@id='TopSellersRows']/a"
        self.discountClass = "discount_pct"
        self.topSellRowXpath = "//*[@id='TopSellersRows']"
        self.discountXpath = "a/div/div[@class='discount_pct']"
        self.originalPriceXpath = "../div/div[@class='discount_original_price']"
        self.discountPriceXpath = "../div/div[@class='discount_final_price']"
        self.lastGameXpath = "//*[@id='NewReleasesRows']/a[15]"




    def navigateToTopSelling(self):
        Wait.WaitXpath(self.actionTitleXpath, self.WaitTime)
        ButtonOperations.ClickButtonXpath(self.topSellXpath)

    def findLowestDiscount(self):
        Wait.WaitXpath(self.topSellRowXpath, self.WaitTime)
        topSellRow = ElementOperations.findOneElement.byXpath(self, self.topSellRowXpath)
        discountElems = ElementOperations.findManyElements.byXpath(self, self.discountXpath, topSellRow)
        sortedDisc = ActionPageLogic.SortDiscountElems().get(discountElems)
        gamesPageDiscount = sortedDisc[0][1]                                                                                            # %
        gamesPagePrice = ElementOperations.findOneElement.byXpath(self, self.originalPriceXpath, sortedDisc[0][0]).text                 # WithoutDiscount
        gamesPageDiscountPrice = ElementOperations.findOneElement.byXpath(self, self.discountPriceXpath, sortedDisc[0][0]).text         # WithDiscount
        data = [gamesPageDiscount, gamesPagePrice, gamesPageDiscountPrice]
        sortedDisc[0][0].click()
        return(data)

    def findHigestDiscount(self):
        Wait.WaitXpath(self.topSellRowXpath, self.WaitTime)
        topSellRow = ElementOperations.findOneElement.byXpath(self, self.topSellRowXpath)
        discountElems = ElementOperations.findManyElements.byXpath(self, self.discountXpath, topSellRow)
        sortedDisc = ActionPageLogic.SortDiscountElems().get(discountElems)
        gamesPageDiscount = sortedDisc[-1][1]                                                                                            # %
        gamesPagePrice = ElementOperations.findOneElement.byXpath(self, self.originalPriceXpath, sortedDisc[-1][0]).text                 # WithoutDiscount
        gamesPageDiscountPrice = ElementOperations.findOneElement.byXpath(self, self.discountPriceXpath, sortedDisc[-1][0]).text         # WithDiscount
        data = [gamesPageDiscount, gamesPagePrice, gamesPageDiscountPrice]
        sortedDisc[-1][0].click()
        return(data)
        #ADD RATED CONTENT BANNER




from framework import BaseElement
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, GetText, MouseOperations
from common import jsonGetter
import time
from pageObjects.pages.Logic import  ActionPageLogic
from framework.BaseElement import *

class ActionPage:
    def __init__(self):
        self.WaitTime = 10
        self.actionTitleXpath = "//div[1]/div[7]/div[4]/div[1]/div[3]/div[1]/h2"
        self.topSellXpath = "//*[@id='tab_select_TopSellers']/div"
        self.pageXpath = "//*[@id='TopSellers_links']/span[6]"
        self.gamesXpath = "//*[@id='TopSellersRows']/a"
        self.discountClass = "discount_pct"
        self.discountClassBlock = "discount_block"

        self.topSellRowXpath = "//*[@id='TopSellersRows']"
        self.dicountXpath = "/a/div/div[@class='discount_pct']"

    def navigateToTopSelling(self):
        Wait.WaitXpath(self.actionTitleXpath, self.WaitTime)
        ButtonOperations.ClickButtonXpath(self.topSellXpath)

    def findHigestDiscount(self):
        Wait.WaitXpath(self.pageXpath, self.WaitTime)
        ButtonOperations.ClickButtonXpath(self.pageXpath)
        time.sleep(2)
        games = ElementOperations.findManyElements.byXpath(self, self.gamesXpath)
        topSellRow = ElementOperations.findOneElement.byXpath(self, self.topSellRowXpath)
        discountElems = ElementOperations.findManyElements.byClass(self, self.discountClass, topSellRow)

        x = []
        for elem in discountElems:
            b = [elem, elem.text]
            x.append(b)
        x.sort(key= lambda x: x[1])

        x[0][0].click()
        pass




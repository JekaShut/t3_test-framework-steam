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
        self.pageXpath = "//*[@id='TopSellers_links']/span[1]"
        self.gamesXpath = "//*[@id='TopSellersRows']/a"
        self.discountClass = "discount_pct"

        self.topSellRowXpath = "//*[@id='TopSellersRows']"
        self.discountXpath = "/a/div/div[@class='discount_pct']"
        self.discountPriceXpath = "../div/div[@class='discount_final_price']"




    def navigateToTopSelling(self):
        Wait.WaitXpath(self.actionTitleXpath, self.WaitTime)
        ButtonOperations.ClickButtonXpath(self.topSellXpath)

    def findLowestDiscount(self):
        Wait.WaitXpath(self.pageXpath, self.WaitTime)
        ButtonOperations.ClickButtonXpath(self.pageXpath)
        time.sleep(2)
        games = ElementOperations.findManyElements.byXpath(self, self.gamesXpath)
        topSellRow = ElementOperations.findOneElement.byXpath(self, self.topSellRowXpath)
        discountElems = ElementOperations.findManyElements.byClass(self, self.discountClass, topSellRow)
        sortedDisc = ActionPageLogic.SortDiscountElems().get(discountElems)
        #gamesPagePrice = ElementOperations.findOneElement.byXpath(self, self.discountPriceXpath, sortedDisc[0][0]).text
        gamesPagePrice = sortedDisc[0][0].find_element_by_xpath(self.discountPriceXpath).text
        sortedDisc[0][0].click()
        return(gamesPagePrice)

        #assert gamePagePrice == gamesPagePrice + " USD"

        #добавить ожидания
        #Добавить валюту в зависимости от локализации
        #Сравнить процент, начальную и послескидочную сумму
        #ADD RATED CONTENT BANNER

        pass




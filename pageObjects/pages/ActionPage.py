from framework import BaseElement
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ManyItems, GetText, MouseOperations
from common import jsonGetter
import time

class ActionPage:
    def __init__(self):
        self.WaitTime = 10
        self.actionTitleXpath = "//div[1]/div[7]/div[4]/div[1]/div[3]/div[1]/h2"
        self.topSellXpath = "//*[@id='tab_select_TopSellers']/div"

    def navigateToTopSelling(self):
        Wait.WaitXpath(self.actionTitleXpath, self.WaitTime)
        ButtonOperations.ClickButtonXpath(self.topSellXpath)

    def findHigestDiscount(self):
        pass
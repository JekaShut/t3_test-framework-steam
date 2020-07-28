from framework import BaseElement
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, GetText, MouseOperations
from common import jsonGetter
import time
from pageObjects.pages.Logic import  ActionPageLogic
from framework.BaseElement import *


class GamePage:
    def __init__(self):
        self.discountPriceOnPageXpath = "//div[@class='game_area_purchase_game_wrapper']/div/div/div/div/div/div[@class='discount_final_price']"

    def getPrices(self):
        time.sleep(2)
        gamePagePrice = ElementOperations.findOneElement.byXpath(self, self.discountPriceOnPageXpath).text
        return(gamePagePrice)
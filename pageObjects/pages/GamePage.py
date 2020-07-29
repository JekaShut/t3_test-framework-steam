from framework import BaseElement
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

    def getPrices(self):
        logger.info("Waiting for the DOM to load the class")
        Wait.WaitXpath(self.DiscountXpath, self.WaitTime)
        gamePageDiscount = ElementOperations.findOneElement.byXpath(self, self.DiscountXpath).text
        gamePagePrice = ElementOperations.findOneElement.byXpath(self, self.PriceOnPageXpath).text
        gamePageDiscountPrice = ElementOperations.findOneElement.byXpath(self, self.discountPriceOnPageXpath).text
        gameData = [gamePageDiscount, gamePagePrice, gamePageDiscountPrice]
        logger.info("Getting element data from the page: " + ", ".join(gameData))
        return(gameData)
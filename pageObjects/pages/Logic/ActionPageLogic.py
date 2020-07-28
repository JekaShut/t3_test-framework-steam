from framework import BaseElement
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, GetText, MouseOperations
from common import jsonGetter


class findDiscounts:
    def byXpath(self, games, Xpath):
        discounts = []
        for game in games:
            try:
                disc = game.find_element_by_xpath(Xpath)
                discounts.append(game)
            except:
                pass
        return(discounts)




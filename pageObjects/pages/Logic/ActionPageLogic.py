from framework import BaseElement
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, GetText, MouseOperations
from common import jsonGetter

class SortDiscountElems:
    def get(self, discountElems):
        x = []
        for elem in discountElems:
            b = [elem, elem.text]
            x.append(b)
        x.sort(key= lambda x: x[1])
        return(x)
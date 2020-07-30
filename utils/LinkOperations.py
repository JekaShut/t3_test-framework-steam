from framework.BaseElement import *


class OpenLink:
    def __init__(self, link):
        driver.get(link)

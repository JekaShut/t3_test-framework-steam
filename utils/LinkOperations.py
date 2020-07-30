from framework.BaseElement import *


class OpenLink:
    def __init__(self, link):
        RunBrowser().driver.get(link)

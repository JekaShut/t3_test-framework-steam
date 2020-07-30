from framework.BaseElement import *


class ClickButtonClass:
    def __init__(self, ButoonClass):
        toClick = RunBrowser().driver.find_element_by_class_name(ButoonClass)
        toClick.click()


class ClickButtonXpath:
    def __init__(self, ButtonXpath):
        toClick = RunBrowser().driver.find_element_by_xpath(ButtonXpath)
        toClick.click()


class ClickFromManyByXpathText:
    def __init__(self, ButtonsXpath, text):
        toClick = RunBrowser().driver.find_elements_by_xpath(ButtonsXpath)
        for elem in toClick:
            if elem.text == text:
                elem.click()
            else:
                pass

from framework.BaseElement import *


class ClickButtonClass:
    def __init__(self, ButoonClass):
        toClick = driver.find_element_by_class_name(ButoonClass)
        toClick.click()


class ClickButtonXpath:
    def __init__(self, ButtonXpath):
        toClick = driver.find_element_by_xpath(ButtonXpath)
        toClick.click()


class ClickFromManyByXpathText:
    def __init__(self, ButtonsXpath, text):
        toClick = driver.find_elements_by_xpath(ButtonsXpath)
        for elem in toClick:
            if elem.text == text:
                elem.click()
            else:
                pass

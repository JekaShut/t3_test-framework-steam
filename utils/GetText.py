from framework.BaseElement import *


class GetText:

    def byXpath(self, Xpath):
        element = driver.find_element_by_xpath(Xpath)
        return (element.text)

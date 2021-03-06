from framework.BaseElement import *


class findOneByText:
    def byclass(self, byclass, text):
        elements = RunBrowser().driver.find_elements_by_class_name(byclass)
        for elem in elements:
            if elem.text == text:
                return(elem)


class findManyElements:
    def byXpath(self, Xpath, element=RunBrowser().driver):
        elements = element.find_elements_by_xpath(Xpath)
        return(elements)

    def byClass(self, byClass, element=RunBrowser().driver):
        try:
            element = element.find_elements_by_class_name(byClass)
            return(element)
        except:
            pass


class findOneElement:

    def byXpath(self, Xpath, element):
        elementReturn = element.find_element_by_xpath(Xpath)
        return(elementReturn)

    def byClass(self, byClass, element= RunBrowser().driver):
        try:
            element = element.find_elements_by_class_name(byClass)
            return(element)
        except:
            pass

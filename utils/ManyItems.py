from framework.framework import *


class findOneByText:
    def byclass(self, byclass, text):
        elements = driver.find_elements_by_class_name(byclass)
        for elem in elements:
            if elem.text == text:
                return(elem)




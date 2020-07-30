from framework.BaseElement import *
from selenium.webdriver.common.action_chains import ActionChains
from common import jsonGetter

BROWSER = jsonGetter.GetJson.getConfig("actualBrowser")


class MoveMouseXpath:
    def __init__(self, Xpath):
       element = driver.find_element_by_xpath(Xpath)
       hov = ActionChains(driver).move_to_element((element)).perform()


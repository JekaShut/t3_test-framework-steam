from selenium.webdriver.common.action_chains import ActionChains

from common import jsonGetter
from framework.BaseElement import *

BROWSER = jsonGetter.GetJson.getConfig("actualBrowser")


class MoveMouseXpath:
    def __init__(self, Xpath):
        element = RunBrowser().driver.find_element_by_xpath(Xpath)
        hov = ActionChains(RunBrowser().driver).move_to_element((element)).perform()

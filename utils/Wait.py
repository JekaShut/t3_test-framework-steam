from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from framework.BaseElement import *


class WaitClass:
    def __init__(self, ClassName, time):
        wait = WebDriverWait(RunBrowser().driver, time)
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, ClassName)))


class WaitXpath:
    def __init__(self, Xpath, time):
        wait = WebDriverWait(RunBrowser().driver, time)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, Xpath)))


class WaitXpathLocated:
    def __init__(self, Xpath, time):
        wait = WebDriverWait(RunBrowser().driver, time)
        element = wait.until(EC.presence_of_element_located(By.XPATH, Xpath))

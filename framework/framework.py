from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import json


BROWSERS = ["ChromeBrowser", "FireFoxBrowser"]


class ChromeBrowser():
    def runBrowser(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return(driver)


class FireFoxBrowser():
    def runBrowser(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return(driver)


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BrowserFactory(metaclass=Singleton):        
    @staticmethod
    def getBrowser(browsertype):
        
        try:
            if browsertype == BROWSERS[BROWSERS.index(browsertype)]:
                
                driver = ChromeBrowser().runBrowser()
                # driver.set_window_size(get.resolutionH, get.resolutionW)
                # driver.maximize_window()
                
                return(driver)
            if browsertype == BROWSERS[BROWSERS.index(browsertype)]:
                driver = FireFoxBrowser().runBrowser()
                # driver.set_window_size(get.resolutionH, get.resolutionW)
                # driver.maximize_window()
                return(driver)
            raise AssertionError("Browser not found")
        except AssertionError as _e:
            print(_e)


class RunBrowser(metaclass=Singleton):
    def __init__(self, actualBrowser="ChromeBrowser"):
        
        if actualBrowser in BROWSERS:
            BROWSERindex = BROWSERS.index(actualBrowser)
        else:
            raise Exception("Такого браузера нет!")
        self.driver = BrowserFactory.getBrowser(BROWSERS[BROWSERindex])


driver = RunBrowser().driver


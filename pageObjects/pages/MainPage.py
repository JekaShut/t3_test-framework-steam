from framework import BaseElement
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, GetText, MouseOperations
from common import jsonGetter
import time
from logger.logger import Logger

logger = Logger(logger="BaseTest").getlog()


LOCAL = jsonGetter.GetJson.get("LOCAL")
SITE = jsonGetter.GetJson.get("SITE")
actualBrowser = jsonGetter.GetJson.get("actualBrowser")
EnglishName = "English (английский)"
RussianName = "Русский (Russian)"

class MainPage:
    def __init__(self):
        self.WaitTime = 10
        self.DownloadButtonClass = "header_installsteam_btn_content"
        self.DropDownXpath = "//*[@id='global_action_menu']/span"
        self.DropDownMenuButtonsXpath = "//*[@id='global_action_menu']/div/div/a"
        self.MainLogoXpath = '//div[@id["global_header"]]/div/div[@class["logo"]]/span[@id["logo_holder"]]'
        self.menuXpath = "//*[@id='genre_tab']/span/a[1]"
        self.actionXpath = "//*[@id='genre_flyout']/div/div[2]/a[1]"
        self.indieXpath = "//*[@id='genre_flyout']/div/div[2]/a[2]"


    def setLang(self):
        logger.info("TRYING TO SET LANG")
        logger.info("Trying to click language dropdown button")
        ButtonOperations.ClickButtonXpath(self.DropDownXpath)
        if LOCAL == "en":
            logger.info("LOCAL IS ENGLISH. Trying to set it")
            logger.info("Click to button: " + EnglishName)

            ButtonOperations.ClickFromManyByXpathText(self.DropDownMenuButtonsXpath, EnglishName)

        if LOCAL == "ru":
            logger.info("LOCAL IS RUSSIAN. Trying to set it")
            logger.info("Click to button: " + RussianName)
            ButtonOperations.ClickFromManyByXpathText(self.DropDownMenuButtonsXpath, RussianName)


    def clickButtonToDownload(self):
        logger.info("Waiting for the DOM to load the class")
        Wait.WaitXpath(self.MainLogoXpath, self.WaitTime)
        logger.info("Trying to click download button")
        ButtonOperations.ClickButtonClass(self.DownloadButtonClass)

    def moveMouseToMenu(self):
        logger.info("Trying to move mouse to menu")
        MouseOperations.MoveMouseXpath(self.menuXpath)

    def clickAction(self):
        logger.info("Waiting for the DOM to load the class")
        Wait.WaitXpath(self.actionXpath, self.WaitTime)
        logger.info("Trying to click Action button")
        ButtonOperations.ClickButtonXpath(self.actionXpath)

    def clickIndie(self):
        logger.info("Waiting for the DOM to load the class")
        Wait.WaitXpath(self.indieXpath, self.WaitTime)
        logger.info("Trying to click Indie button")
        ButtonOperations.ClickButtonXpath(self.indieXpath)





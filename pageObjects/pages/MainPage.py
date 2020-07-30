from common import jsonGetter
from logger.logger import Logger
from utils import ButtonOperations, Wait, MouseOperations
from framework.BaseElement import TimeoutException, NoSuchElementException

logger = Logger(logger="MainPage").getlog()

LOCAL = jsonGetter.GetJson.getConfig("LOCAL")
SITE = jsonGetter.GetJson.getConfig("SITE")
actualBrowser = jsonGetter.GetJson.getConfig("actualBrowser")
EnglishName = jsonGetter.GetJson.getData("enText")
RussianName = jsonGetter.GetJson.getData("ruText")
ru = jsonGetter.GetJson.getData("ru")
en = jsonGetter.GetJson.getData("en")


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
        try:
            ButtonOperations.ClickButtonXpath(self.DropDownXpath)
        except TimeoutException:
            logger.error("Cannot find element! " + self.DropDownXpath)

        if LOCAL == en:
            logger.info("LOCAL IS ENGLISH. Trying to set it")

            try:
                logger.info("Click to button: " + EnglishName)
                ButtonOperations.ClickFromManyByXpathText(self.DropDownMenuButtonsXpath, EnglishName)
                #Wait.WaitXpath(self.DropDownXpath, self.WaitTime)
            except TimeoutException:
                logger.error("Cannot find element! " + self.DropDownMenuButtonsXpath)

        if LOCAL == ru:
            logger.info("LOCAL IS RUSSIAN. Trying to set it")
            try:
                logger.info("Click to button: " + RussianName)
                ButtonOperations.ClickFromManyByXpathText(self.DropDownMenuButtonsXpath, RussianName)
                #Wait.WaitXpath(self.DropDownXpath, self.WaitTime)
            except TimeoutException:
                logger.error("Cannot find element! " + self.DropDownMenuButtonsXpath)

    def clickButtonToDownload(self):
        logger.info("Waiting for the DOM to load the class")
        try:
            Wait.WaitXpath(self.MainLogoXpath, self.WaitTime)
        except TimeoutException:
            logger.error("Cannot find element! " + self.MainLogoXpath)
        logger.info("Trying to click download button")
        ButtonOperations.ClickButtonClass(self.DownloadButtonClass)

    def moveMouseToMenu(self):
        logger.info("Trying to move mouse to menu")
        try:
            Wait.WaitXpath(self.menuXpath, self.WaitTime)
        except TimeoutException:
            logger.error("Cannot find element! " + self.menuXpath)
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

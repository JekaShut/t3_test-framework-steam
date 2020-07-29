from framework import BaseElement
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations, GetText, MouseOperations
from common import jsonGetter
import time


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
        ButtonOperations.ClickButtonXpath(self.DropDownXpath)
        if LOCAL == "en":
            ButtonOperations.ClickFromManyByXpathText(self.DropDownMenuButtonsXpath, EnglishName)

        if LOCAL == "ru":
            ButtonOperations.ClickFromManyByXpathText(self.DropDownMenuButtonsXpath, RussianName)

    def clickButtonToDownload(self):
        Wait.WaitXpath(self.MainLogoXpath, self.WaitTime)
        ButtonOperations.ClickButtonClass(self.DownloadButtonClass)

    def moveMouseToMenu(self):
        MouseOperations.MoveMouseXpath(self.menuXpath)

    def clickAction(self):
        Wait.WaitXpath(self.actionXpath, self.WaitTime)
        ButtonOperations.ClickButtonXpath(self.actionXpath)

    def clickIndie(self):
        Wait.WaitXpath(self.indieXpath, self.WaitTime)
        ButtonOperations.ClickButtonXpath(self.indieXpath)





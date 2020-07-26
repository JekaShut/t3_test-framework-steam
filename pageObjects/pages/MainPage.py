from framework import framework
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ManyItems, GetText
from common import jsonGetter
import time


LOCAL = jsonGetter.GetJson.get("LOCAL")
SITE = jsonGetter.GetJson.get("SITE")
actualBrowser = jsonGetter.GetJson.get("actualBrowser")
EnglishName = "English (английский)"
RussianName = "Русский (Russian)"

class MainPage:
    def __init__(self):
        self.WaitTime = 20
        self.DownloadButtonClass = "header_installsteam_btn_content"
        self.DropDownXpath = "//*[@id='global_action_menu']/span"
        self.DropDownMenuButtonsXpath = "//*[@id='global_action_menu']/div/div/a"
        self.MainLogoXpath = '//div[@id["global_header"]]/div/div[@class["logo"]]/span[@id["logo_holder"]]'

    def setLang(self):
        ButtonOperations.ClickButtonXpath(self.DropDownXpath)
        if LOCAL == "en":
            ButtonOperations.ClickFromManyByXpathText(self.DropDownMenuButtonsXpath, EnglishName)

        if LOCAL == "ru":
            ButtonOperations.ClickFromManyByXpathText(self.DropDownMenuButtonsXpath, RussianName)


    def clickButtonToDownload(self):
        Wait.WaitXpath(self.MainLogoXpath, self.WaitTime)
        # Тут долго сидел с wait, не получается сделать ожидание в этом месте, постоянно вылетает ошибка
        #time.sleep(7)
        ButtonOperations.ClickButtonClass(self.DownloadButtonClass)
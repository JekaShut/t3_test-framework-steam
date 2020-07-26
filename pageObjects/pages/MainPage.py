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
        self.ButtonClass = "header_installsteam_btn_content"

    def setLang(self):

        if LOCAL == "en":
            ButtonOperations.ClickButtonXpath("//*[@id='global_action_menu']/span")
            ButtonOperations.ClickFromManyByXpathText("//*[@id='global_action_menu']/div/div/a", EnglishName)


        if LOCAL == "ru":
            ButtonOperations.ClickButtonXpath("//*[@id='global_action_menu']/span")
            ButtonOperations.ClickFromManyByXpathText("//*[@id='global_action_menu']/div/div/a", RussianName)


    def clickButtonToDownload(self):
        Wait.WaitXpath('//div[@id["global_header"]]/div/div[@class["logo"]]/span[@id["logo_holder"]]', 20)
        # Тут долго сидел с wait, не получается сделать ожидание в этом месте, постоянно вылетает ошибка
        #time.sleep(7)
        ButtonOperations.ClickButtonClass(self.ButtonClass)
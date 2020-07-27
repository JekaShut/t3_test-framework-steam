from framework import BaseElement
from common import jsonGetter
from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ManyItems
import time
from pageObjects.pages import DownloadPage, MainPage
from pageObjects.SystemAsserts import fileIsDownloaded


LOCAL = jsonGetter.GetJson.get("LOCAL")
SITE = jsonGetter.GetJson.get("SITE")
actualBrowser = jsonGetter.GetJson.get("actualBrowser")



class TestRunbrowser():
    def test_runbrowser(self):
        BaseElement.RunBrowser(actualBrowser)
        LinkOperations.OpenLink(SITE)

    def test_lang(self):
        MainPage.MainPage().setLang()

class TestSteamDownload:

    def test_steampageload(self):
        MainPage.MainPage().clickButtonToDownload()
        DownloadPage.DownloadPage().clickButtonToDownload()

    def test_fileIsDownloaded(self):
        assert fileIsDownloaded.fileIsDownloaded().checkFile() == True


class TestStopTests:
    def test_TearDown(self):
        time.sleep(2)
        StopBrowser.stop()

from framework import framework
from Common import jsonGetter
from Utils import LinkOperations, ButtonOperations, StopBrowser, DownloadFile, Wait




class TestSteamDownload:

    def test_steampageload(self):
        framework.RunBrowser(jsonGetter.GetJson.get("actualBrowser"))
        LinkOperations.OpenLink(jsonGetter.GetJson.get("SITE"))
        ButtonOperations.ClickButtonClass("header_installsteam_btn_content")
        Wait.WaitClass("about_install", 10)


    def test_steamdownload(self):
        ButtonOperations.ClickButtonClass("about_install")


# class TestStopTests:
#     def test_TearDown(self):
#         StopBrowser.stop()

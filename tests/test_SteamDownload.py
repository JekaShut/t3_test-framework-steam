from framework import framework
from Common import jsonGetter
from Utils import LinkOperations, ButtonOperations, StopBrowser, DownloadFile, WaitClass




class TestSteamDownload:

    def test_steampageload(self):
        framework.RunBrowser(jsonGetter.GetJson.actualBrowser)
        LinkOperations.OpenLink(jsonGetter.GetJson.SITE)
        ButtonOperations.ClickButtonClass("header_installsteam_btn_content")
        WaitClass.Wait("about_install", 10)


    def test_steamdownload(self):
        ButtonOperations.ClickButtonClass("about_install")


# class TestStopTests:
#     def test_TearDown(self):
#         StopBrowser.stop()

from common import jsonGetter
import time
import os


class fileIsDownloaded:
    def __init__(self):
        self.sleepTime = 2
        self.DIR = jsonGetter.GetJson.getConfig("DIR")
        self.file = "SteamSetup.exe"

    def checkFile(self):
        time.sleep(self.sleepTime)
        directory = os.listdir(self.DIR)
        for file in directory:
                if file == self.file:
                    installed = True
        return(installed)
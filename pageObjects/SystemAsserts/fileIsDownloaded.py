from common import jsonGetter
import time
import os


class fileIsDownloaded:
    def __init__(self):
        self.sleepTime = 2
        self.DIR = jsonGetter.GetJson.get("DIR")

    def checkFile(self):
        time.sleep(self.sleepTime)
        directory = os.listdir(self.DIR)
        for file in directory:
                if file == "SteamSetup.exe":
                    installed = True
        return(installed)
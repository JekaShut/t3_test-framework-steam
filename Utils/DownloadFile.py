from framework.framework import driver

class DownloadFile:
    def __init__(self):
        self.preferences = {"download.default_directory": "/"}
        self.options = driver.ChromeOptions()
        self.options.add_experemental_option
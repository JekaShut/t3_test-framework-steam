from framework.BaseElement import *


class stop:
    def __init__(self):
        RunBrowser().driver.close()
        RunBrowser().driver.quit()

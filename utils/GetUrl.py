from framework.BaseElement import *


class Get:
    def CurrentUrl(self):
        url = RunBrowser().driver.current_url
        return (url)

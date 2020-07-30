from framework.BaseElement import *


class Get:
    def CurrentUrl(self):
        url = driver.current_url
        return (url)

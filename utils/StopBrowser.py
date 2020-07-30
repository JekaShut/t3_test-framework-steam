from framework.BaseElement import *


class stop:
    def __init__(self):
        driver.close()
        driver.quit()

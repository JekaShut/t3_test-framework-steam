from framework.framework import *


class stop:
    def __init__(self):
        driver.close()
        driver.quit()
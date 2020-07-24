from framework.framework import driver


class stop:
    def __init__(self):
        driver.close()
        driver.quit()
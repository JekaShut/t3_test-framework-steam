from framework.framework import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Wait:
    def __init__(self, ClassName, time):
        wait = WebDriverWait(driver, time)
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, ClassName)))

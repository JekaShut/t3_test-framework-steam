import time

from logger.logger import Logger
from utils import StopBrowser

logger = Logger(logger="TC-quit").getlog()


class TestStopTests:
    def test_TearDown(self):
        time.sleep(2)
        logger.info("Trying to stop browser")
        StopBrowser.stop()

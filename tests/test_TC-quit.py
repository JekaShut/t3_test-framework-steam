from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations
import time
from logger.logger import Logger

logger = Logger(logger="TC-quit").getlog()



class TestStopTests:
    def test_TearDown(self):
        time.sleep(2)
        logger.info("Trying to stop browser")
        StopBrowser.stop()
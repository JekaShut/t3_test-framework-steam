from utils import LinkOperations, ButtonOperations, StopBrowser, Wait, ElementOperations
import time




class TestStopTests:
    def test_TearDown(self):
        time.sleep(2)
        StopBrowser.stop()
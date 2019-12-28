import os
import sys
import pytest

from get_data import get_data

sys.path.append(os.getcwd())
from Base.getDriver import GetDriver
from page.mss_home import MsshomePage
from page.mss_send import SendPage
class TestMms:
    def setup_class(self):
        # com.android.mms/.ui.ConversationList
        self.driver = GetDriver().get_driver("com.android.mms",".ui.ConversationList")
        self.home_mss = MsshomePage(self.driver)
        self.send_mss = SendPage(self.driver)
    def teardown_class(self):
        self.driver.quit()



    @pytest.mark.parametrize('a,b',get_data())
    def test_01(self,a,b):
        self.home_mss.new_mss()
        print(get_data())
        self.send_mss.send_user(a,b)
        date = self.send_mss.get_assert()

        assert b in [x.text for x in date]
        self.send_mss.black()






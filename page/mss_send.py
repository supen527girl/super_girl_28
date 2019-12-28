import time

import page
from Base.Base import Base


class SendPage(Base):
    def  __init__(self,driver):
        Base.__init__(self,driver)
    def send_user(self,text,te):
        time.sleep(3)
        self.send_text(page.new_user_xpath,text)
        time.sleep(1)
        self.send_text(page.send_mas_xpath,te)
        self.click_btn(page.click_mas_xpath)
    def get_assert(self):
        return self.find_eles(page.assert_mss_id)
    def black(self):
        self.click_btn(page.black_mms)



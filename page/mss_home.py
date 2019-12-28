import page
from Base.Base import Base


class MsshomePage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    # 点击新建短信
    def new_mss(self):
        self.click_btn(page.new_mas_id)



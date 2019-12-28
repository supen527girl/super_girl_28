from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver
    def find_ele(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
    def find_eles(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))
    def click_btn(self,loc,timeout=5,poll=0.5):
        self.find_ele(loc,timeout,poll).click()
    def send_text(self,loc,text,timeout=5,poll=0.5):
        self.find_ele(loc,timeout,poll).clear()
        self.find_ele(loc,timeout,poll).send_keys(text)

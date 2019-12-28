class GetDriver:
    def get_driver(self,a,b):
        # 导包
        import time

        from appium import webdriver

        Capabilities = dict()
        Capabilities["platformName"] = "Android"
        Capabilities["platformVersion"] = "5.1"
        Capabilities["deviceName"] = "模拟器"
        Capabilities["appPackage"] = a
        Capabilities["appActivity"] = b
        Capabilities["unicodeKeyboard"] = True
        Capabilities["resetKeyboard"] = True

        # 创建驱动对象
        return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=Capabilities)


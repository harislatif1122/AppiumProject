from appium import webdriver

class AppiumDriver:
    def __init__(self):
        desired_cap = {
            "platformName": "Android",
            "appium:platformVersion": "11",
            "appium:app": "C:\\Users\\HP\\Desktop\\Appium_Apps\\Arriva_updated.apk"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(20)

    def get_driver(self):
        return self.driver
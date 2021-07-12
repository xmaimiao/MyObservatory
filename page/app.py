from appium import webdriver
from page.basepage import BasePage
from page.indexpage import Index


class App(BasePage):
    _package = 'hko.MyObservatory_v1_0'
    _activity = '.myObservatory_app_SplashScreen'

    def start(self):
        '''
        启动APP
        :return:
        '''
        if self.driver == None:
            caps = dict()
            caps["platformName"] = 'Android'
            caps["deviceName"] = '127.0.0.1:7555'
            caps["platformVersion"] = '6.0.1'
            caps["appPackage"] = self._package
            caps["automationName"] = 'uiautomator2'
            caps["appActivity"] = self._activity
            caps["noReset"] = 'true'
            # 启动之前不关闭APP
            caps["dontStopAppOnReset"] = 'true'
            caps["chromedriverExecutable"] = 'C:\\Users\\xingmaimiao\\AppData\\Local\\Programs\\Appium\\chromedriver2.20.exe'
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self.driver.start_activity(self._package,self._activity)
        self.set_implicitly_wait(3)
        return self

    def stop(self):
        '''
        停止APP
        '''
        self.driver.close_app()

    def goto_index(self):
        '''
        進入首頁
        '''
        return Index(self.driver)





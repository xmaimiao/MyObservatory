'''
BasePage:存放一些基本的放大，比如：初始化 driver，find查找元素
'''
import json
import logging
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    logging.basicConfig(level=logging.INFO)
    _params = {}

    def __init__(self,driver:WebDriver = None):
        self.driver = driver
        self.env = yaml.safe_load(open("../data/env.yaml"))

    def find(self,by,locator):
        logging.info(f"find：{locator}")
        if by == None:
            result=self.driver.find_element(*locator)
        else:
            result = self.driver.find_element(by,locator)
        return result

    def finds(self,by,locator):
        logging.info(f"find_eles：{locator}")
        return self.driver.find_elements(by,locator)

    def find_and_click(self,by,locator):
        logging.info("click")
        self.find(by,locator).click()

    def find_scroll_click(self,text):
        logging.info("find_scroll_click")
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector()'
                                                               f'.text("{text}").instance(0));').click()
    def find_scroll(self,text):
        logging.info("find_scroll")
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector()'
                                                               f'.text("{text}").instance(0));')

    def webdriver_wait_click(self, by,locator, timeout=20):
        logging.info(f"webdriver_wait_click：{locator},timeout：{timeout}")
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((by,locator)))


    def set_implicitly_wait(self,second):
        self.driver.implicitly_wait(second)

    def step(self, path, name):
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)[name]
        # ${}的參數轉化
        raw_data = json.dumps(steps)
        # 替換傳入參數
        for key,value in self._params.items():
            raw_data = raw_data.replace("${"+key+"}",value)
        steps = json.loads(raw_data)
        for step in steps:
            # 替換測試環境dev/uat
            step["locator"] = str(step["locator"]).\
                replace("testing-studio", self.env["testing-studio"][self.env["default"]])
            if "action" in step.keys():
                action = step["action"]
                if "wait_click" == action:
                    self.webdriver_wait_click(step["by"],step["locator"])
                if "click" == action:
                    self.find_and_click(step["by"],step["locator"])
                if "text" == action:
                    text = self.find(step["by"], step["locator"]).get_attribute('text')
                    return text
                if "find_scroll_click" == action:
                    self.find_scroll_click(step["locator"])
                if "find_scroll" == action:
                    self.find_scroll(step["locator"])


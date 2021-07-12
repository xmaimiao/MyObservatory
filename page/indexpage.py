from common.contants import index_dir
from page.basepage import BasePage
from page.the_9_day_forecast import The_9_day_forecast


class Index(BasePage):

    def click_serve(self):
        '''
        点击左上角“服务”图标
        '''
        self.step(index_dir,"click_serve")
        return self


    def goto_the_9_day_forecast(self):
        '''
        进入the_9_day_forecast
        '''
        self.step(index_dir,"goto_the_9_day_forecast")
        return The_9_day_forecast(self.driver)



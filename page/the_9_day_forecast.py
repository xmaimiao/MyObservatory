from common.contants import the_9_day_forecast_dir
from page.basepage import BasePage



class The_9_day_forecast(BasePage):
    def get_the_n_day_humidity(self,date):
        '''
        获取第N日的相对湿度
        :param date: 如 "14 Jul"格式的数据
        '''
        self._params["date"] = date
        return self.step(the_9_day_forecast_dir,"get_the_n_day_humidity")

    def back_to_index(self):
        '''
        返回index页
        '''
        from page.indexpage import Index
        return Index(self.driver)

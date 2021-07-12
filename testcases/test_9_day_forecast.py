import pytest
import yaml
from common.contants import test_9_day_forecast_dir
from page.app import App
import pytest_check as check
import datetime

def get_data(option):
    '''
    获取yaml测试数据
    '''
    with open(test_9_day_forecast_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas

class TestLogin:
    #输出当前月份简称 及后天为第N天
    now = datetime.datetime.now()
    month = now.strftime('%b')
    date = str((now + datetime.timedelta(days=abs(2))).strftime("%d"))

    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.index = self.app.start().goto_index()

    def teardown(self):
        self.app.stop()

    def test_get_the_humidity_of_the_day_after_tomorrow(self):
        '''
        验证获取后天的相对湿度
        '''
        date = self.date+' '+self.month
        result = self.index.click_serve().goto_the_9_day_forecast().get_the_n_day_humidity(date)
        if check.is_in('%', result, f"无法获取相对湿度"):
            print(f"后天的相对湿度为{result}")

    @pytest.mark.parametrize("data", get_data("test_get_the_n_day_humidity"))
    def test_get_the_n_day_humidity(self,data):
        '''
        验证获取当月第几号的相对湿度
        '''
        date = data["date"]+' '+self.month
        result = self.index.click_serve().goto_the_9_day_forecast().get_the_n_day_humidity(date)
        if check.is_in('%', result, f"无法获取相对湿度"):
            print(f"{data['date']}日的相对湿度为{result}")
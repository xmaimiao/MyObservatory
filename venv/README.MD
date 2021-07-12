测试用例：
1.获取后天的相对湿度。
2.根据输入的日期获取对应日期的相对湿度。

测试框架pytest+selenium简述：
  1.测试步骤的数据驱动，将测试步骤封装到yaml文件中管理。
  2.测试数据的数据驱动，将测试数据封装到yaml文件中管理。

pytest.ini配置文件：
终端执行pytest生成对应的测试reports。

环境配置参数：./venv/requirement.txt文件中

该代码驱动mumu模拟器运行，需终端连接模拟器，配置相应Chromedriver后执行代码，其中参数如下；
caps["platformName"] = 'Android',
caps["deviceName"] = '127.0.0.1:7555'

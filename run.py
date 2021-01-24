from common import method   # 导入公共方法
from test_data import test_data  # 导入测试数据
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

url=test_data.data.get('url')
username = test_data.data['username']
password=test_data.data.get('password')
key=test_data.data.get('key')
print(url,username,password,key)
num=method.search_func(driver,url,username,password,key)
if key in num:
    print('搜索结果正确')
else:
    print('搜索结果不正确')
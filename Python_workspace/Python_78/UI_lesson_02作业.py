from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)    # 隐形等待

url = 'http://erp.lemfix.com/login.html'
driver.get(url)

# 获取页面的标题
# page_title=driver.title
# if page_title == "柠檬ERP":
#     print('这个页面的标题是：{}'.format(page_title))
# else:
#     print('这个用例执行不通过')

driver.find_element_by_id('username').send_keys('test123')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()   # 记住用户名
driver.find_element_by_id('btnSubmit').click()
time.sleep(2)

'''
xpath元素定位方法：
1.绝对路径： /html/body/div/div/div[1]/a/small
2.相对路径：//*[@id="username"]
'''
# driver.find_element_by_xpath('//*[@id="username"]').send_keys('test123')

# # 确认登录用户名
# page_name = driver.find_element_by_xpath('//p').text
# if page_name == "测试用户":
#     print('登录的用户名字是：{}'.format(page_name))
# else:
#     print('这个用例执行不通过')


driver.find_element_by_xpath("//span[text()='零售出库']").click()

id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')  # 找到元素，获取id的属性
id_frame = id_li+'-frame'  # 找到iframe的id
# print(id_frame)
driver.switch_to.frame(id_frame)    #通过iframe的id进行切换
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_frame)))   # 通过元素定位

# 接下来就是针对子页面的操作
driver.find_element_by_xpath("//*[@name='searchNumber']").send_keys('841')   #输入841
driver.find_element_by_xpath("//span[text()='查询']").click()   # 点击查询

time.sleep(2)  # 隐式等待结合强制等待使用
num=driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']/td[@field='number']/div").text
# print(num)
if '841' in num:
    print('搜索结果正确')
else:
    print('搜索结果不正确')
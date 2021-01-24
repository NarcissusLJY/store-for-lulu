from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://erp.lemfix.com')
driver.maximize_window()
driver.find_element_by_id('username').send_keys('test123')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
driver.find_element_by_id('btnSubmit').click()
time.sleep(2)
# page_name=driver.find_element_by_xpath('//p').text
# print('这个登录用户是：{}'.format(page_name))
driver.find_element_by_xpath("//span[text()='零售出库']").click()

id_li=driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')
id_iframe = id_li+'-frame'
driver.switch_to.frame(id_iframe)

driver.find_element_by_xpath("//input[@name='searchNumber']").send_keys('710')
driver.find_element_by_xpath("//span[text()='查询']").click()
time.sleep(2)
num=driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']/td[@field='number']/div").text
if '710' in num:
    print("搜索测试通过")
else:
    print("搜索测试不通过")
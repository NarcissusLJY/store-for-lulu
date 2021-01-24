import time
# 打开会话的函数
def open_url(driver,url):
    driver.get(url)
    driver.maximize_window()


# 登录的函数
def login_func(driver,username,password):
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()   # 记住用户名
    driver.find_element_by_id('btnSubmit').click()

# 查询的函数
def search_func(driver,url,username,password,key):
    open_url(driver,url)
    login_func(driver,username,password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()

    id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')  # 找到元素，获取id的属性
    id_frame = id_li+'-frame'
    driver.switch_to.frame(id_frame)
    driver.find_element_by_xpath("//*[@name='searchNumber']").send_keys(key)   #输入841
    driver.find_element_by_xpath("//span[text()='查询']").click()   # 点击查询

    time.sleep(2)  # 隐式等待结合强制等待使用
    num=driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']/td[@field='number']/div").text
    return num

from selenium import webdriver
import time


# driver=webdriver.Chrome()
# driver.get("http://baidu.com")
# driver.maximize_window()  # 浏览器最大化
# time.sleep(2)
# driver.get("http://taobao.com")
# driver.back()
# driver.forward()
# driver.refresh()
# driver.close()
#

# url = 'http://baidu.com'
# driver.get(url)
# s=driver.page_source
# print(s)
# driver.quit()
# driver.find_element_by_id()


import requests
url = 'https://www.baidu.com/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
res=requests.get(url = url,headers = header)
# print(res.text)
res1=res.content.decode('utf8')
print(res1)

# url = 'https://www.jd.com/'
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
# response = requests.get(url=url,headers=header)
# result1=response.text
# print(result1)

# 安装第三方库 pip install request
import requests,pprint
# # 注册
# url_reg = "http://8.129.91.152:8766/futureloan/member/register"
# header_reg = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
# data_reg = {"mobile_phone": "15915541863","pwd": "lemon123456"}
#
# result = requests.post(url=url_reg,headers=header_reg,json=data_reg)
# response = result.json()
# print(response)

# # 登录
# url_login = "http://8.129.91.152:8766/futureloan/member/login"
# header_login = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
# data_login = {"mobile_phone": "15915541863","pwd": "lemon123456"}
#
# result = requests.post(url=url_login,headers=header_login,json=data_login)
# response = result.json()
# pprint.pprint(response)

# 充值
# token取值方法一  ---字典嵌套取值
# token=response['data']['token_info']['token']
# id=response['data']['id']
# token取值方法二   ---jsonpath
# 安装jsonpath第三方库  pip install jsonpath
import jsonpath
# token=jsonpath.jsonpath(response,"$..token")[0]   # $表示最外层  ..表示匹配任意次数（递归搜索）
# id=jsonpath.jsonpath(response,"$..id")[0]
# # print(token,id)
# url_recharge = "http://8.129.91.152:8766/futureloan/member/recharge"
# header_recharge = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json","Authorization":"Bearer"+" "+token}
# data_recharge = {"member_id": id,"amount":100}
# result = requests.post(url=url_recharge,headers=header_recharge,json=data_recharge)
# response = result.json()
# print(response)


# 封装函数
# def login_func(url,json):
#     header_login = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
#     result = requests.post(url=url, headers=header_login, json=data)
#     response = result.json()
#     return response
#
# url_login = "http://8.129.91.152:8766/futureloan/member/login"
# data_login = {"mobile_phone": "15915541863","pwd": "lemon123456"}
# re = login_func(url=url_login,json=data_login)
# pprint.pprint(re)
#
#
# def recharge_func(url,data,header):
#     result1 = requests.post(url=url,json=data,headers=header)
#     response1 = result1.json()
#     return response1
#
# token = jsonpath.jsonpath(re, "$..token")[0]
# id = jsonpath.jsonpath(re, "$..id")[0]
# header_recharge = {"X-Lemonban-Media-Type": "lemonban.v2",
#                    "Content-Type": "application/json",
#                     "Authorization": "Bearer" + " " + token}
# url_recharge = "http://8.129.91.152:8766/futureloan/member/recharge"
# data_recharge = {"member_id": id,"amount":100}
# re1 = recharge_func(url=url_recharge,json=data_recharge,headers=header_recharge)
# print(re1)


# # 面试题  访问百度
# def api_baidu(url,headers):
#     result =requests.get(url=url,headers=headers)
#     response = result.content.decode("utf8")
#     return response
# url = "https://www.baidu.com/"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
# res = api_baidu(url=url,headers=headers)
# print(res)

# 访问京东
# url_jd="https://www.jd.com/"
# headers_jd={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
#
# response=requests.get(url=url_jd,headers=headers_jd)
# result1=response.text
# # result2=response.content.decode("utf8")
# print(result1)


# import openpyxl
# openpyxl.load_workbook()


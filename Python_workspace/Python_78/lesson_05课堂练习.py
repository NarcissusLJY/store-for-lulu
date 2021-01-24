import requests
import pprint
# 注册
# url_reg = "http://8.129.91.152:8766/futureloan/member/register"
# header_reg = {'X-Lemonban-Media-Type':'lemonban.v2',
#               'Content-Type':'application/json'}
# body_reg = {"mobile_phone": "15915267738",
#              "pwd": "lemon123",
#              "type":"1",
#              "reg_name":"鹿鹿"}
# response = requests.post(url=url_reg,headers=header_reg,json=body_reg)
# pprint.pprint(response.json())

# 登录
url_log = "http://8.129.91.152:8766/futureloan/member/login"
header_log = {'X-Lemonban-Media-Type':'lemonban.v2',
              'Content-Type':'application/json'}
body_log = {"mobile_phone": "15915267738",
             "pwd": "lemon123",}
response = requests.post(url=url_log,headers=header_log,json=body_log)
pprint.pprint(response.json())
res = response.json()

# 充值
# 方法一：字典取值
# member_id = res['data']['id']
# token = res['data']['token_info']['token']
# url_rec = "http://8.129.91.152:8766/futureloan/member/recharge"
# header_rec = {'X-Lemonban-Media-Type':'lemonban.v2',
#               'Content-Type':'application/json',
#               'Authorization':'Bearer '+token}
# body_rec = {"member_id":member_id,
#             "amount":100}
# response = requests.post(url=url_rec,headers=header_rec,json=body_rec)
# pprint.pprint(response.json())

# 方法二
import jsonpath
# member_id = jsonpath.jsonpath(res,"$..id")[0]
# token = jsonpath.jsonpath(res,"$..token")[0]
# url_rec = "http://8.129.91.152:8766/futureloan/member/recharge"
# header_rec = {'X-Lemonban-Media-Type':'lemonban.v2',
#               'Content-Type':'application/json',
#               'Authorization':'Bearer '+token}
# body_rec = {"member_id":member_id,
#             "amount":100}
# response = requests.post(url=url_rec,headers=header_rec,json=body_rec)
# pprint.pprint(response.json())

# 访问百度请求
# url_baidu = "https://www.baidu.com"
# header_baidu = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
# res=requests.get(url=url_baidu,headers=header_baidu)
# # print(res.text)
# print(res.content.decode("utf8"))

# # 带参数的请求
# url_baidu = "https://www.baidu.com/s"
# header_baidu = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
# param = {'wd':"柠檬班"}
# res=requests.get(url=url_baidu,headers=header_baidu,params=param)
# print(res.content.decode("utf8"))


# 封装函数
def api_func(url,json):
    token = jsonpath.jsonpath(res,"$..token")[0]
    header_rec = {'X-Lemonban-Media-Type':'lemonban.v2',
                  'Content-Type':'application/json',
                  'Authorization':'Bearer '+token}
    response = requests.post(url=url_rec,headers=header_rec,json=body_rec)
    result = response.json()
    return result

member_id = jsonpath.jsonpath(res,"$..id")[0]
url_rec = "http://8.129.91.152:8766/futureloan/member/recharge"
body_rec = {"member_id": member_id,
            "amount": 100}
res1 = api_func(url_rec,body_rec)
print(res1)

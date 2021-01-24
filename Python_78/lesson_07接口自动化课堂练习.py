from Python_78 import lesson_06openpyxl


"""
{'case_id': 1, 'url': 'http://api.lemonban.com/futureloan/member/register', 'data': '{"mobile_phone":"13552440101","pwd":"12345678","type":1,"reg_name":"34254sdfs"}', 'expect_result': '{"code": 0, "msg": "OK"}'}
"""


def excute_func(filename,sheetname):
    cases = lesson_06openpyxl.read_data('test_case_api.xlsx','register')
    for case in cases:
        case_id = case.get('case_id')
        url = case.get('url')
        data = case.get('data')
        data = eval(data)
        expect_result = case.get('expect_result')
        expect_result = eval(expect_result)
        expect_msg = expect_result.get('msg')
        real_result = lesson_06openpyxl.api_func(url_api=url,data_api=data)
        real_msg = real_result.get('msg')
        print(expect_msg)
        print(real_msg)
        if expect_msg == real_msg:
            final_result = "Passed"
            print('第{}条测试用例执行通过'.format(case_id))
        else:
            final_result = "Failed"
            print('第{}条测试用例执行不通过'.format(case_id))
        print("*"*20)
        lesson_06openpyxl.write_result(filename,sheetname,final_result,case_id+1,8)
# excute_func('test_case_api.xlsx','register')



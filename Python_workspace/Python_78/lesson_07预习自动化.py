import requests,openpyxl

# 发送请求
def api_func(url_api,data_api):
    header = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'}
    response=requests.post(url=url_api,json=data_api,headers=header)
    result=response.json()
    return result
# 写入数据
def write_result(filename,sheetname,final_result,row,column):
    wb = openpyxl.load_workbook(filename)
    sheet = wb[sheetname]
    sheet.cell(row=row,column=column).value = final_result
    wb.save(filename)

# 读取表格
def read_data(filename,sheetname):
    wb = openpyxl.load_workbook(filename)
    sheet = wb[sheetname]
    # 获取最大行数
    max_row = sheet.max_row
    cases = []
    for i in range(2,max_row+1):
        case = dict(
        case_id = sheet.cell(row=i,column=1).value,
        url = sheet.cell(row=i,column=5).value,
        data = sheet.cell(row=i,column=6).value,
        expect_result = sheet.cell(row=i,column=7).value)
        cases.append(case)
    return cases
def excute_func(filename,sheetname):
    cases=read_data(filename,sheetname)   # 赋值
    for case in cases:                                # for循环取出每一条用例
        case_id = case.get('case_id')                 # 获取id,url,data,expect
        url = case.get('url')
        data = case['data']
        data1 = eval(data)
        expect = case.get('expect_result')
        expect1 = eval(expect)
        expect_msg = expect1.get('msg')
        real_result = api_func(url_api=url,data_api=data1)           # 用获取的数据发送接口请求
        real_msg = real_result.get('msg')                     # 获取实际的响应信息
        print("期望结果是：{}".format(expect_msg))
        print("实际结果是：{}".format(real_msg))
        if real_msg == expect_msg:
            print("第{}条测试用例通过".format(case_id))             # print("这条测试用例执行通过")
            final_result = "Passed"
        else:
            print("第{}条测试用例不通过".format(case_id))
            final_result = "Failed"
        print("*"*20)
        write_result(filename,sheetname,final_result,case_id+1,8)
excute_func('test_case_api.xlsx','login')







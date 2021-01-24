# # 1.把字符串转成列表
# str1 = "Python是最棒的语言"
# list1 = list(str1)
# print(list1)

# str2 = "hello_world_python"
# list1 = str2.split("_")
# print(list1)

# 2.完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和
# sum1 = 0
# for i in range(100):
#     sum1 += i
# print(sum1)

# # 用户输入
# num = int(input("请输入数字："))
# sum = 0
# for i in range(num):
#     sum += i
# print(sum)

# # 封装函数
def cal(data):
    sum1 = 0
    for i in range(data):
        sum1 += i
    return sum1
res = cal(100)
print("这个整数序列相加的和是：{}".format(res))


# # 3.定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套
# def object(data):
#     # if type(data)==list or type(data)==dict or type(data)==str:
#     if isinstance(data,list) or isinstance(data,dict) or isinstance(data,str):
#         len1 = len(data)
#         if len1 > 5:
#             print('True')
#         else:
#             print('False')
#     else:
#         print("数据类型不符")
# object(["hello","world",1,2,3,4])
#

# # 列表 list  可变可重复，包含任意类型，有固定索引
# '''增加  append insert extend
#    删除  remove pop
#    修改  list1[0] = "" 重新赋值
#
# '''
# list1 = ["hello","world",123,["happy","new","year"]]
# print(list1[0:2])


# # 元组 tuple  不可变可重复，包含任意类型，有索引
# # 拓展 强制转换
# tuple1 = ("hello","world",123,["happy","new","year"])
# list2 = list(tuple1)
# list2[0] = "Hello"
# tuple2 = tuple(list2)
# print(tuple2)
#
# print(("hello","world",123,["happy","new","year"]))
# # 等同于
# a = ("hello","world",123,["happy","new","year"])
# print(a)


# # 字典 dict { }  无序，Key不可重复,可增删改
# dict1 = {"name":"鹿鹿","age":18,"gender":"female","score":[100,99,98]}
# # 取值
# print(dict1["name"])
# # 等同于
# print(dict1.get("name"))
# # 取 key value items
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# # 增加
# dict1["hobby"] = "reading"
# print(dict1)
# # 修改
# dict1["age"] = 19
# print(dict1)
# # 删除
# dict1.pop("score")
# print(dict1)
# # 统计有几个元素
# print(len(dict1))
# # 拓展 增加多个元素
# dict1.update({"height":160,"weight":47})
# print(dict1)

# # 集合 set  {}
# # 1.单个元素 2.元素不能重复，使用场景，给列表去重
# # set1 = {"lulu","fafa","lemon","yuanyuan","lemon"}
# # print(set1)
#
# list2 = ["lulu","fafa","lemon","yuanyuan","lemon"]
# set2 = set(list2)
# print(set2)
# list3 = list(set2)
# print(list3)

'''
控制流：   if判断   for循环
if判断语法
if条件：    ---如果成立则进入下面的执行语句-分支
    字代码（执行语句）
elif条件：   ---如果成立则进入下面的执行语句-分支
    字代码（执行语句）
elif条件：        ---注意：elif可以没有，可以有多个
    字代码（执行语句）
    .
    .
    .
else:    --- else是没有条件的
    字代码（执行语句）

'''

# money = int(input("请输入你的存款："))
# if money>=200:
#     print("买房")
# elif money>=100:
#     print("买车")
# elif money>=50:
#     print("买股票")
# elif money>=20:
#     print("买零食")
# else:
#     print("加油，打工人")

# for循环
# list3 = ["lulu","fafa","lemon","yuanyuan"]
# str1 = "快乐"
# for m in list3:
#     print(m)
#     for n in str1:
#         print(n)

# list4 = ["新","年","好"]
# str2 = "12"
# for m in list4:
#     for n in str2:
#         print(m)
#         print(n)

# 跳过数据里的某个元素
# break continue

# list3 = ["lulu","fafa","lemon","等","yuanyuan"]
# for elem in list3:
#     if elem == "等":
#         break
#     print(elem)

# list3 = ["lulu","fafa","lemon","等","yuanyuan"]
# for elem in list3:
#     if elem == "等":
#         continue
#     print(elem)

# range函数 与for循环结合使用，用来生成一个整数序列
# 用逗号隔开

# for a in range(0,10,2):
#     print(a)


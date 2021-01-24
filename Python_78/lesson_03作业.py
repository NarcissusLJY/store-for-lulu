# # 1.a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面 -- if
# a = [1,2,'6','summer']
# if "i" in a:
#     print(True)
# else:
#     print(False)


# # 2.dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5，注：num表示课堂人数。如果大于5，输出人数。
# dict_1 = {"class_id": 45,'num': 20}
# a = dict_1['num']
# if a>5:
#     print("上课人数为：{}".format(a))
# else:
#     print("上课人数不足5人")





'''
3.	list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']，列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。并且把字典都存在新的 list中，最后打印最终的列表。
方法1： 手动扩充--字典--存放在列表里面；{} --简单
方法2： 自动--dict（）--不强制-- for循环 ，list.append()
'''
# 方法1
# list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
# dict1 = {"name":"肥兔","gender":"male","age":18,"city":"天津"}
# dict2 = {"name":"鹿鹿","gender":"female","age":18,"city":"江苏"}
# dict3 = {"name":"Freestyle","gender":"male","age":18,"city":"杭州"}
# dict4 = {"name":"等","gender":"male","age":18,"city":"广东"}
# dict5 = {"name":"地球","gender":"male","age":18,"city":"深圳"}
# dict6 = {"name":"阑珊","gender":"female","age":18,"city":"湖南"}
# dict7 = {"name":"柠檬","gender":"female","age":18,"city":"广西"}
# list2 = [dict1,dict2,dict3,dict4,dict5,dict6,dict7]
# print(list2)

# 方法2-1
# list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
# dict1 = dict(name="肥兔",gender="male",age=18,city="天津")
# dict2 = dict(name="鹿鹿",gender="female",age=18,city="江苏")
# dict3 = dict(name="Freestyle",gender="male",age=18,city="杭州")
# dict4 = dict(name="等",gender="male",age=18,city="广东")
# dict5 = dict(name="地球",gender="male",age=18,city="深圳")
# dict6 = dict(name="阑珊",gender="female",age=18,city="湖南")
# dict7 = dict(name="柠檬",gender="female",age=18,city="广西")
# list2 = []
# for name in list1:
#     if name == dict1['name']:
#         list2.append(dict1)
#     elif name == dict2['name']:
#         list2.append(dict2)
#     elif name == dict3['name']:
#         list2.append(dict3)
#     elif name == dict4['name']:
#         list2.append(dict4)
#     elif name == dict5['name']:
#         list2.append(dict5)
#     elif name == dict6['name']:
#         list2.append(dict6)
#     else:
#         list2.append(dict7)
# print(list2)

# 方法2-2
# list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
# list2 = []
# for i in list1:
#     dict1 = dict(name=i, gender="male", age=18, city="天津")
#     list2.append(dict1)
# print(list2)

# 方法2-3
# list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
# list2 = ['male','female','male','male','male','female','female']
# list3 = ['18','18','18','18','18','18','18']
# list4 = ['天津','江苏','杭州','广东','深圳','湖南','广西']
# list5 = []
# for i in range(7):
#     dict1 = dict(name=list1[i],gender=list2[i],age=list3[i],city=list4[i])
#     list5.append(dict1)
# print(list5)


# # 4.for循环遍历其他的数据类型 --字典
# b = {"name":"鹿鹿","age":18,"gender":"female","city":"江苏","score":[100,99,98]}
# for key,value in b.items():
#     print("{}:{}".format(key,value))

# # 4.for循环遍历其他的数据类型 --元组
# tuple1 = ("hello","world",123,["happy","new","year"])
# for elem in tuple1:
#     print(elem)





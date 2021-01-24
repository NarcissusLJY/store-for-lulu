# 列表  list
# list = ["hello","world",123,["happy","new","year"]]
# print(list)
#
# # 索引
# # 列表索引返回的数据类型是该元素原有的数据类型
# print(list[0])
# print(len(list))
#
# # 切片
# print(list[0:2])
#
# # 增加元素
# # 1、在列表的最后增加一个元素
# list.append("快乐")
# print(list)
#
# # 2、在指定的索引位置增加一个元素
# list.insert(1,"K")
# print(list)
#
# # 3、同时加多个元素，列表合并
# list.extend(["Marco","purple love"])
# print(list)
#
# # 删除元素
# # 删除指定的内容位置
# list.remove("K")
# print(list)
#
# # 删除指定的索引位置
# list.pop(5)
# print(list)
#
# # 修改某个元素
# list[5] = "love"
# print(list)
#
# my_list = ["啊哈哈","拉拉","开心"]
# # new_elem = my_list.append("快乐")
# # print(my_list)
# # print(new_elem)  # new_elem  得到的结果是none
#
# # 删除  得到的结果是none
# # remove
# elem = my_list.remove("啊哈哈")
# print(elem)     # elem  得到的结果是none
# print(my_list)
#
# # pop 得到的结果是删除的元素
# elem = my_list.pop(0)
# print(my_list)
# print(elem)   # elem  得到的结果是删除的元素
#
# d = list.insert(1,"K")
# print(d)
#
# e = list.extend(["Marco","purple love"])
# print(e)
#
#
# # clear 清除列表里的元素
# list1 = [1,2]
# print(list1.clear())  # --->返回none
#
# print(list1)   # --->返回[ ]

# 排序  sort  一般对数字进行排序  升序
# list2 = [1,3,6,2]
# a = list2.sort()
# print(list2)
# print(a)   # --->none

# list3 = ["对数组的引用","数组在原数组上进行排序","不生成副本"]
# list3.sort()
# print(list3)

# list4 = ["对数组的引用","数组在原数组上进行排序",[1,3,6,2]]
# list4.sort()
# print(list4)

# # 倒序    .sort(reverse=True)
# list2.sort(reverse=True)
# print(list2)

# print(type(list3))

# a = [1,0.05,"lemonban",(1,2,3),[4,5,6]]
# print(a[-1][-1])


# dict  ---字典  字典的表示方法{key：value,key1:value1,key2:value2} --- 键值对
# 列表存储多个数据的时候，不知道元素具体表达的含义，字典能够表达每个元素的具体意思
# 字典的key是有要求的  1）不能重复 2）key为哈希值，不可变，通常用字符串表示
# c = {"name":"鹿鹿","age":18,"gender":"female","score":[100,99,98]}
# 字典是没有索引和切片的，有索引代表有顺序，列表是有序的，字典是无序的
# print(c['name'])

# 新增一个元素 [new_key]=value  new_key在当前字典不存在---字典是一种可变类型
# c['hobby']="reading"
# print(c)

# 修改一个元素 [old_key]=value  old_key在当前字典存在
# c["age"]=19
# print(c)

# 删除一个元素
# c.pop('score')
# print(c)

# clear
# c.clear()
# print(c)

# del
# del c["age"]
# print(c)

# popitem
# c = {"name":"鹿鹿","age":18,"gender":"female","score":[100,99,98]}
# c.popitem()
# print(c)
#
# # 查询所有的key
# print(c.keys())
# print(type(c.keys()))    # 字典里面key的数据类型是列表
#
# # 查询所有的value
# print(c.values())
#
# # 查询所有的键值对  以元组的形式体现
# print(c.items())

#
# # 更新 update
# # c = {"name":"鹿鹿","age":18,"gender":"female","score":[100,99,98]}
# # d = {"name":"lulu","age":"unknow"}
# c.update(d)
# print(c)
#


#
# # 元组  表示方法： ( )
# print("name","gender")
#
# a = ("name","gender")
# print(a)
#
# # 空元组的表示
# b = ()
# print(type(b))
# print(len(b))
#
# # 1个元素的元组，一定要在元素后面加逗号，如果不加逗号，那么得到的数据类型将是这个元素的数据类型
# c= ("haha",)
# print(len(c))
# print(type(c))
#
# # 元组是不可变的类型
# # d = ('lemonban',)
# # d[0] = ('lemon')
# # print(d)
#
#
# # 元组是有序的，可以通过索引和切片进行操作
#
# # 元组的解包，拆包
# a,b,c = ('lulu','fafa','lemon')
# print(a)
# print(b)
# print(c)




# 集合  表示方法：{ } ，和字典相比是没有key的
# 集合是无序的
# my_set = {"lulu","fafa","lemon"}
# print(my_set)
# print(len(my_set))

# 集合是不可修改的
# my_set[0] = 'lulu'
# print(my_set)

# 可增加
# 可删除

# # 集合的主要作用：是为了去除重复元素
# my_set_01 = {"lulu","fafa","lemon","lulu"}
# print(my_set_01)

#
# # 列表去重  转化成set去重再转化回list   --- 面试题
# my_list = ["lulu","fafa","lemon","lulu"]
# print(list(set(my_list)))
#
# a = {(1,):"lulu"}
# print(a)
#
# b = {(1,2):"lulu"}
# print(b)
#

# if条件语句  表达式：
#     （缩进）条件满足以后要运行的代码
# elif条件表达式2：
#     （缩进）代码2
# elif条件表达式3：
#     （缩进）代码3
# else (没有表达式，剩下所有的情况）：
#    （缩进）else条件满足要运行的代码
# 当其中一个条件满足，其他的条件分支自动屏蔽，不会再运行
# 1个缩进用4个空格
# 4个空格不等于1个tab，pycharm里面可以用

# # 在一个if表达式中，if...elif...else...如果运行了其中一个条件，其他的分支就不会再执行
# if 4>3:
#     print("haha")
# elif 4!=3:
#     print("gaga")
# else:
#     print("lala")

# # if 变量
# # "",[],{},0,False,() 代表的就是条件不成立
# if 1:
#     print("这是1")
# if "":
#     print("这是空字符串")
# if True:
#     print("True")


# if的嵌套



'''
有下面几个数据 ，t1 = ("aa",11)      t2= ("bb",22)    li1 = [("cc",11)]，请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":11,"bb":22}(ps: 元组取值，然后给字典添加key-value)
'''
t1 = ("aa",11)
t2= ("bb",22)
li1 = [("cc",11)]
dict1 = {}
dict1[t1[0]]=t1[1]
dict1[li1[0][0]]=li1[0][1]
dict1[t2[0]]=t2[1]
print(dict1)

# 拼接
li = ["python","java","php"]
li2 = "_".join(li)
print(li2)
# 拆分
li3 = li2.split("_")
print(li3)

# 九九乘法表
for a in range(1,10):
    for b in range(1,a+1):
        print(b,"*",a,"=",a*b,end=" ")
    print()



'''while
使用场景没有for循环多
while循环：不知道循环几次

'''
# 1. 用户输入一个数值，请判断用户输入的是否为偶数？是偶数输出True,不是输出False（提示:input输入的不管是什么，都会被转换成字符串，自己扩展，想办法转换为数值类型，再做判段，）
# a = int(input("请输入一个数字："))
# b = a%2
# if b == 0:
#     print("True")
# else:
#     print("False")

# def cal(a):
#     b= a%2
#     if b == 0:
#         print("True")
#     else:
#         print("False")
# cal(11)

# 2. 现在有列表 li = [‘hello’,‘scb11’,‘!’],通过相关操作转换成字符串：'hello python18 !'（注意点:转换之后单词之间有空格）
# li = ['hello','scb11','!']
# li[1] = "python18"
# str1 = " ".join(li)
# print(str1)

'''
3. 现在有字符串：str1 = 'python hello aaa 123123aabb'
1）请计算 字符串中有多少个'a'      
2）请找出字符串中'123'的下标起始位置
3）请分别判断  'o a'      'he'    'ab'  是否是该字符串中的成员？
'''

# str1 = 'python hello aaa 123123aabb'
# num = str1.count("a")
# print(num)
#
# b = str1.find('123')
# print(b)
#
# print('o a' in 'str1')
# print('he' in 'str1')
# print('ab' in 'str1')

# 或
# str1 = 'python hello aaa 123123aabb'
# list1 = ['o a','he','ab']
# for i in list1:
#     if i in str1:
#         print('{}是该字符串的成员'.format(i))
#     else:
#         print('{}不是该字符串的成员'.format(i))


# 4. 将给定字符串的PHP替换为Python，best_language = "PHP is the best programming language in the world! "
# best_language = "PHP is the best programming language in the world!"
# best = best_language.replace("PHP","Python")
# print(best)

# 5编写代码，提示用户输入1-7七个数字，分别代表周一到周日，如果输入的数字是6或7则为周末，打印输出“今天是周几”
# num = int(input("请输入1-7中的一个数字:"))
# list1 = ["周一","周二","周三","周四","周五","周末","周末",]
# str1= "今天是{}".format(list1[num-1])
# print(str1)

# 或
# num = input("请输入1-7中的一个数字:")
# list1 = ["周一","周二","周三","周四","周五","周末","周末",]
# if num.isdigit():
#     if int(num) in(6,7):
#         print('今天是周末')
#         print('今天是{}'.format(list1[int(num) - 1]))
#     elif int(num) in(1,2,3,4,5):
#         print('今天是{}'.format(list1[int(num)-1]))
# else:
#     print('请输入正确的数字')


'''
6. 现在有一个列表 li2=[1，2，3，4，5]，
     第一步：请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]
     第二步：对li2进行排序处理 
     第三步：请写出删除列表中元素的方法，并说明每个方法的作用
'''
# li2=[1,2,3,4,5]
# li2.insert(0,0)
# li2.insert(4,66)
# li2.extend([11,22,33])
# print('追加元素之后的列表为：{}'.format(li2))
#
# li2.sort()
# print(li2)

# remove 指定列表里的内容删除
# pop  指定列表的索引进行删除
# clear 清空列表里的内容 只剩空列表


'''
7. 切片 
    1、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9] 
    2、s = 'python java php',通过切片获取: ‘java’ 
    3、tu = ['a','b','c','d','e','f','g','h'],通过切片获取 [‘g’,‘b’] 
'''
# li = [1,2,3,4,5,6,7,8,9]
# print(li[2::3])
#
# s = 'python java php'
# lo = s.find("java")
# print(s[lo:lo+4])

# 或
# s = 'python java php'
# li1 = s.split(' ')
# print(li1[1])



#
# tu = ['a','b','c','d','e','f','g','h']
# tu1 = tu[-2]
# tu2 = tu[1]
# list1 = [tu1,tu2]
# print(list1)

'''
8. 有5道题（通过字典来操作）：
    1. 某比赛需要获取你的个人信息，设计一个程序，运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来，
    2、数据存储完了，然后输出个人介绍，格式如下:  我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
    3. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
    4. 平台为了保护你的隐私，需要你删除你的联系方式；
    5. 你为了取得更好的成绩， 你添加了自己的擅长技能，至少需要 3 项。
'''
# dict1 = dict(
# name = input("请输入你的姓名："),
# gender = input("请输入你的性别："),
# age = input("请输入你的年龄："))
# print('我的名字:{},今年{}岁,性别:{},喜欢敲代码'.format(dict1['name'],dict1['age'],dict1['gender']))
# dict1.update({'height':160,'tel_phone':13356567788})
# dict1.pop("tel_phone")
# dict1['擅长的技能'] = ['唱歌','跳舞','睡觉']
# print(dict1)

'''
9. 一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格。
'''
# def price(data):
#     if data >= 50 and data<= 100:
#         discount = 0.1
#         price1 = data*(1-0.1)
#         print("你的折扣是：{}".format(discount),"最终价格是:{}".format(price1))
#     elif data > 100:
#         discount = 0.2
#         price1 = data*(1-0.2)
#         print("你的折扣是：{}".format(discount), "最终价格是:{}".format(price1))
#     else:
#         print("你不能享受折扣，最终价格为:{}".format(data))
# price(100)

'''
11、一个 5 位数，判断它是不是回文数。例如： 12321 是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息。
'''
# if判断
# a = input("请输入一个数字：")
# b = a[::-1]
# if a==b:
#     print("这是一个回文数")
# else:
#     print("这不是一个回文数")

# # 封装函数
# a = input("请输入一个数字：")
# def jud(a):
#     b = a[::-1]
#     if a == b:
#         print("这是一个回文数")
#     else:
#         print("这不是一个回文数")
# jud()

'''
12、现有一个字典： dict = {'name':'小明','age':18,'occup':'students','teacher': {'语文':'李老师','数学':'王老师','英语':'张老师'}}， 请获取到小明同学的名字；然后再获取到小明的数学老师。
'''
# dict = {'name':'小明','age':18,'occup':'students','teacher': {'语文':'李老师','数学':'王老师','英语':'张老师'}}
# print(dict['name'])
# print(dict['teacher']['数学'])

'''
13、设计一个函数，获取一个100以内偶数的纯数字序列，并存到列表里， 然后求这些偶数数字的和。
'''

# def cal(num):
#     list1 = []
#     for num in range(2,num,2):
#         list1.append(num)
#     print(list1)
#     sum1 = 0
#     for i in list1:
#         sum1 += i
#     return sum1
# res = cal(50)
# print(res)


# 14、输出99乘法表，结果如下：（提示嵌套for循环，格式化输出）
# for a in range(1,10):
#     for b in range(1,10):
#         if b<=a:
#             print("{}*{}={}".format(b,a,a*b),end='\t')
#     print()

# 或
# for i in range(1,10):
#      for j in range(1,i+1):
#          print('{}*{}={}'.format(j,i,i*j,end=' '))
#      print('')

# 15、有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？
# list1 = [1,2,3,4]
# count = 0
# for a in list1:
#     for b in list1:
#         for c in list1:
#             if a != b != c:
#                 count += 1
#                 print('互不相同且无重复数字的3位数是：{}{}{}'.format(a,b,c))
# print('互不重复的三位数一共有{}个'.format(count))


# 16、通过函数实现一个计算器，运行程序分别提示用户输入数字1，数字2，然后再提示用户选择 ： 加【1】  减【2】 乘【3】 除【4】，每个方法使用一个函数来实现， 选择后调用对应的函数，然后返回结果。
# def cal():
#     num1 = int(input("请输入数字1或2："))
#     num2 = int(input("请输入数字1或2："))
#     choose = input('请选择：加【1】减【2】乘【3】除【4】')
#     if choose == '1':
#         return num1+num2
#     elif choose == '2':
#         return num1-num2
#     elif choose == '3':
#         return num1*num2
#     elif choose == '4':
#         return num1/num2
#     else:
#         print('没有此选项')
#
# res = cal()
# print(res)

black_list = ['卖茶叶的','卖膜的','卖保险的','卖花生的','卖手机的']
# for i in range(len(black_list)):      #   列表是可变的，index会一直 +=1 ， len(black_list)是不变的，永远是5
#     black_list.pop(0)
# print(black_list)

# 或
# black_list_new = ['卖茶叶的','卖膜的','卖保险的','卖花生的','卖手机的']
# # for i in black_list_new:
# #     black_list.pop(0)
# # print(black_list)
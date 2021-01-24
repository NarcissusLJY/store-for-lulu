# 格式化输出有两种方式：1.str.format() ; 2.str %  %s--字符串，%d--数字，%f--小数
# name = 'fafa'
# gender = 'female'
# hobby = 'lulu'
# age = 18
# print('''--------%s档案---------
# name:%s
# gender:%s
# hobby:%s
# age:%d
# '''%(name,name,gender,hobby,age))


"""
 字符串的操作
1、取值--字符串里的每一个都是元素，每个元素都有自己的位置--索引  从0开始
"""

# 定义一个字符串
# str1 = "hello lemonban!"
# # 取"o"
# print(str1[4])

# # 取最后一个"!"
# print(str1[-1])

# 索引超出范围会报错  index error
# print(str1[18])

# # 取hello， 切片  规则：取头不取尾，所以最后一位要+1
# print(str1[0:5:1])
# print(str1[:5:])

# # 取整个字符串
# print(str1[0:len(str1):1])
# 切片超出范围不会报错，表示一直取到最后一位
# print(str1[0:1000:1])

# print(str1[:])
# print(str1[:-1])

# 步长为-1
# str2 = "欢迎来到 柠檬班！"
# print("{}".format(str2[6:0:-1]))
# print("{}".format(str2[-2:-4:-1]))

# str1[:] 可以复制原来的文本

# # 找到某个元素的索引   index / find

# index找不到会报错，会影响后面代码的运行
# print(str1.index('o'))

# find找不到不会报错，返回-1，不影响后面代码的运行
# print(str1.find('o'))
# print(666)

# # count 统计一个元素出现几次
# print(str1.count("o"))

# # 替换 replace
# print(str1.replace("lemonban","Python"))

# 算数运算符
# + 1、数字的相加 2、字符串的拼接
# print(10+20)
# print("tricy"+"lemon")
# print("tricy"+'100')
# print("tricy"*100)
# print(0.1+0.2)

# 数据类型的转换
# print(type(str(10)))
# print(type(int("123")))
# print(int("123"))
# print(float(2))

# input 获取从控制台输入的内容，输入的任何内容都是字符串
# name = input("请输入名称:")
# print(name)

# num = int(input("请输入数字："))
# print(num+1)

# - 数字相减，不支持字符串
# print(20-10)
#
# # * 1、数字相乘 2、字符串的重复输出
# print(2*3)
# print("i love you"*3000)

# # / 数字的相除，返回结果是float
# print(10/3)

# 幂运算
# print(2**3)

# # 整除
# a = 10//3
# print(a)

# # 模运算 --- 取余数 经常用来判断奇偶数
# a = 10%3
# print(a)

# # 赋值运算 把符号右边的内容赋值给左边的内容 =，+=，-=
# a = 10
# a += 5  # a = a+5
# a -= 10
# a *= 4
# a /= 2
# print(a)

# 比较运算符  > < == <=  >=  !=   结果是布尔值
# print(3 == 3)
#
# a = (1 == 2)
# print(a)
# print(3 !=4)
# print(4<3)
# print("登录成功"=="登录成功")


# 逻辑运算符   and  or  not  与或非
# print(3>4 and 5<9)
# print(3>4 or 5<9)
# print(not 5<9)

# 运算符的先后顺序  优先级  ()的优先级最高
# print(not 2!=3 and 3<4 or 5==4)

# # 成员运算符
# str2 = "hello Python"
# print("P" in str2)

# # 字符串操作  大小写
# a = "hello World"
# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a.capitalize())
# print(a.swapcase())   # 大小写转换

# # join  --- 字符串的拼接
a = "#".join(['http://baidu.com/login','post','narcissus','123'])
print(a)
#
# # split  --- 字符串的拆分
b = a.split("#")
print(b)
#
# strip  --- 字符串去掉首尾的空格
word = "  wefw wefki "
c = word.strip()
print("处理后的结果：{}".format(c))
#
# # isdigit  判断是否是数字，返回布尔值
# print(c.isdigit())
#
# # islower  判断是否是小写，返回布尔值
# print(c.islower())
#

str2 = "字符串反转后再输出"
print(str2[::-1])
print(str2[::1])
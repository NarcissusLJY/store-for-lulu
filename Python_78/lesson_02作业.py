# name = input("请输入姓名:")
# age = input("请输入年龄:")
# gender = input("请输入性别:")
# print('''*******************
# 姓名:{}
# 性别:{}
# 年龄:{}
# *******************
# '''.format(name,gender,age))


# 2、现在有字符串：str1 = 'python hello aaa 123123aabb'
# 1）请取出并打印字符串中的'python'。
# 2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？
# 3）替换python为 “lemon”.
# 4) 找到aaa的起始位置

str1 = "python hello aaa 123123aabb"
print(str1[0:6:1])
print("o a" in "python hello aaa 123123aabb")
print("he" in "python hello aaa 123123aabb")
print("ab" in "python hello aaa 123123aabb")
print(str1.replace('python', 'lemon'))
print(str1.find('aaa'))


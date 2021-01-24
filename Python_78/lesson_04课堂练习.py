'''
函数：将常用的代码以固定的格式封装成一个独立的模块，只要知道这个模块的名字就可以重复使用它
作用：提高代码的复用率
格式：
def 函数名(参数列表):
    函数体（真正实现具体功能的代码）
函数名（）
参数化  形参 实参
'''
#
# def cal(a,b):
#     res = a*b
#     print(res)
# cal(1,2)


# def good_job(salary,bonus,subsidy,*args,**kwargs):    # --->定义函数  --形参
#     print("参数salary:{}".format(salary))
#     print("参数bonus:{}".format(bonus))
#     print("参数subsidy:{}".format(subsidy))
#     print("参数args:{}".format(args))
#     print("参数kwargs:{}".format(kwargs))
#     sum1 = salary+bonus+subsidy
#     for a in args:
#         sum1 += a
#     for b in kwargs:
#         sum1 += kwargs.get(b)
#     print("工资总和是:{}".format(sum1))
#     if sum1 > 10000:
#         print("冲鸭打工人！")
#     else:
#         print("告辞")
# good_job(8000, 2000, 800, 111, 222, 333, a=50, b=60, c=70)  # --->调用函数 --实参

# 定义函数的返回值
# 定义返回值后，用变量接收函数的调用的时候，变量接收的是函数的返回值
# 返回值可以没有--None，可以有多个，多个的返回值之间用逗号隔开，用元组接收

def good_job(salary,bonus,subsidy=500,*args,**kwargs):
    sum1 = salary + bonus + subsidy
    for a in args:
        sum1 += a
    for b in kwargs:
        sum1 += kwargs.get(b)
    return sum1
result = good_job(8000, 2000, 800, 111, 222, 333, a=50, b=60, c=70)
if result>=10000:
    print("冲鸭打工人！")
else:
    print("告辞")



# def gs(j,g=1,*args):
#     sum = j+g
#
#     for a in args:
#         for b in a:
#             num+=b
#         count += a
#     sum = count+num
#     return sum
# res = gs(200,100,[1,2],1,2)
# print(res)

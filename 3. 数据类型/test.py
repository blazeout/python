"""
基本数据类型:整形, 浮点型, 字符串
特殊数据类型:字典, 元组, 列表, 集合
"""

#  整形
import string

num = 1
#  浮点型
num_2 = 1.1
#  字符串
name = "wjh"

print(num, num_2, name)
print(type(num_2))

a = b = c = 1
print(a, b, c)

num1 = 10
num2 = 3
print(num1 - num2)
#  "/" 是带有小数的除法, "//" 是整除
print(num1 // num2)

flag = True
flag1 = False

if not (flag1 and flag):
    print("yes")

print(flag and flag1, flag or flag1)

num3 = 1
List = [1, 2, 3, 4, 5]
print(num3 in List)
print(num3 not in List)

name = "往"
x = "号"
x += name

print(x, len(x))
print(x[0])
print(x[-2])
print("我的名字是%s, 年龄是%d" % ("wjh", 20))
print("{}:{}:{}".format("192.168.0.1", "8080", 1))


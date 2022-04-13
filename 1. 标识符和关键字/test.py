import keyword

# 标识符
from typing import List

name = "王嘉豪"
Name = "王嘉豪"
中文 = "王嘉豪"
print(中文)

"""
打印关键字
"""
print(keyword.kwlist)
# 缩进
if name == "王嘉豪":
    print("nice")
    print("====")
print("ok")


def guess_name():
    name1 = input("请输入姓名")
    print(name1)


guess_name()


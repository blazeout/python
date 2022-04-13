"""
if , else, 和 elif
"""

user = input("请输入姓名")
if user == "admin":
    print("登陆成功")
elif user == "root":
    print("登录失败")
else:
    print("滚")

age = int(input("请输入年龄"))

if age > 60:
    print("进去吧")
elif 20 >= age >= 10:
    print("小屁孩啊滚")
else:
    print("还可以交钱吧")

price = int(input("输入钱"))
height = int(input("输入身高"))
if height >= 180:
    if price >= 10:
        print("高富帅你好")
    else:
        print("搞搞的人呢")
else:
    print("滚啊")





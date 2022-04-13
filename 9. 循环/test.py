"""
for item in 可迭代的数据:
    功能代码段
"""

strs = "123"
dict1 = {"name": "wjh", "age": 20}

for char in strs:
    print(char)

for i in range(len(strs)):
    print(strs[i])

#  取出所有的键
for key in dict1.keys():
    print(key)

#  取出所有的值
for value in dict1.values():
    print(value)

#  取出所有的键和值
for key, value in dict1.items():
    print(key, value)

"""
while 循环
    while 条件:
        代码段
"""
i = 0
while i < 10:
    print("gg")
    i += 1
    if i == 5:
        break

#  for range循环, 写法和切片一样~~~
for i in range(1, 9, 2):
    print(i, " ", end="")

#  快速生成列表
temp = list(range(1, 9))
print(temp)

#  continue 和 break 一个继续一个跳出






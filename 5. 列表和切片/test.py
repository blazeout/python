"""
列表 : 中括号[], 可以放任意值
"""

#  空的
list1 = []
#  带有值的列表
list2 = [1, 2, 3, 4, 5]
#  啥都可以放
list3 = [1, "王嘉豪", True, 0.1, [1, 2, 3]]
print(list3[2], list3[4][1])

list4 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#   step 不能为0
print(list4[0:8:1])

print(type(list4[2:7]))
print(list4[-7:-2])

print(list4[0:9:2])

#  list的append追加
# list4.reverse()
# print(list4)
list4.append("zzz")
print(list4)

#  insert 插入
list4.insert(1, "wjh")
print(list4)

#  extend 增加
list5 = [1, 2, 3]
list4.extend(list5)
print(list4)

#  remove删除从左至右匹配的第一个值
list4.remove(2)
print(list4)

#  pop有返回值, pop最后一个
print(list4.pop())
ret = list4.pop()
#  del 删除第一个值
del list4[0]
print(list4)

#  reverse 反转
list3.reverse()

print(list4.index(4))

#  count 计算这个value在列表中出现的次数
print(list4.count(1))

list4[0] = "get"
print(list4)


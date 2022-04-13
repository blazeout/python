"""
字典 : 映射关系的数据结构
key : 只支持 int, float, bool, 字符串, 元组
value : 支持任意的值
"""

hashtable = dict()
hashtable[1] = 1
print(hashtable[1])

dict1 = {"name": "王嘉豪", "key1": "hello", "key2": "get", "key3": "whirlwind", 11: 11}
print(dict1)

#  pop方法
dict1.pop("key1")
print(dict1)

#  popitem删除最后一对键值对
dict1.popitem()
print(dict1)

#  取出所有的key
for key in dict1.keys():
    print(key)

#  取出所有的value
for value in dict1.values():
    print(value)

#  同时取出所有的key和值
for key, value in dict1.items():
    print(key, value)

    


string = "王嘉豪"

#  start_with()判断字符串是否以xxx开头
print(string.startswith("王"))

#  end_with()判断字符串是否以xxx结尾
print(string.endswith("xxx"))

#  isdigit()判断字符串是否是存数字
print(string.isdigit())

#  strip()去除字符串两边的指定字符
print(string.strip())

#  lower()将字符串变成小写
str1 = "LOW"
print(str1.lower())

#  upper()将字符串变成大写
str2 = "low"
print(str2.upper())

#  replace()字符串内容的替换
print(str2.replace("w", "W"))

#  split()切割字符串
str3 = "你好呀,zzz,nnn"
print(str3.split(","))


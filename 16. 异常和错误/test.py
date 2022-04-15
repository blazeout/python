"""
异常和错误
"""

#  异常和错误会导致后面的代码不会被执行, 如果还想执行后面的代码需要进行异常捕捉
try:
    print(5 / 1)
except Error:
    print("有错误")
else:
    #  加了一个else是如果try成功else也会执行
    print("成功执行")
finally:
    #  不管有没有出错都会执行这一段代码
    print("我是finally语句")

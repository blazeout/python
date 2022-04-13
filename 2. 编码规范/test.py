"""
1. 类名采用驼峰命名法, 每个首字母都要大写, 不能使用下划线
2. 函数名只能用小写和下划线, 不能用大写
3. 顶级定义之间要空两行
4. 定义类后面包含一个文档字符串, 且与代码空一行
5. 两个类之间用两个空格来进行分割
6. 变量名等号两边各有一个空格 如 name = "xxx"
7. 函数内部之间的等号两边不需要空格
8. 函数和函数之间需要两个空格
9. #号注释离开两个空格
"""


#  这个是Hello的函数
def hello_world(self, name="wjh", age=18):
    print("hello")


def get_name(self):
    name = input("请输入姓名")
    print(name)


class HelloWorld:
    """这个类是用来打印Hello, World! 的"""

    print("Hello, World!")


class PrintDirect:
    """这个类用来打印 Direct 的"""

    print("Direct")

"""
类的构造函数使用
"""


class Test:
    #  构造函数, 会在类加载的时候自动运行, 常作用于一些初始化的工作~
    def __init__(self):
        print("构造函数会自动运行")

    name = "wjh"

    #  实例方法, 参数中必须带有self, 不在类中的方法不需要self
    def test1(self):
        print("hello, world")

    def hello(self):
        self.test1()
        self.__world()

    #  私有示例方法, 只能在类中调用
    def __world(self):
        print("我是私有方法")


test1 = Test()
# test1.test1()
print(test1.name)
test1.hello()

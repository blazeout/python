"""
类 : class, 第一个字母大写驼峰式命名
"""


class HumanBeing:
    name = "王嘉豪"  # 公有属性
    __age = 18      # 私有属性

    def run(self):
        print(self.name, "正在跑")
        print(self.__age)


human = HumanBeing()
print(human.name)
print(human.run())



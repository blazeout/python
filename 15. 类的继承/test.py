"""
类的继承和多态
多态意思是不同的子类调用同一个方法有不同的结果
"""


class Phone:
    color = "白色"

    #  手机可以打电话
    def call(self):
        print("拨打电话")

    def __hello(self):
        print("你好呀")


class IPhone(Phone):
    """继承类后可以使用父类的属性和公有方法"""

    #  iphone比较牛逼, 可以玩游戏
    def play_game(self):
        print("玩撸啊撸")

    #  重写父类的方法, 但又想调用父类的方法怎么办呢?
    def call(self):
        print("zzzz")


iPhone = IPhone()
iPhone.call()
iPhone.play_game()
print(iPhone.color)
phone = Phone()

#  这样即可~~, 通过类名调用
Phone.call(iPhone)


class StartPay:
    def start(self, method):
        method.pay()


class Wechat:
    def pay(self):
        print("使用微信支付")


class AliPay:
    def pay(self):
        print("使用支付宝支付")


wechat = Wechat()
alipay = AliPay()

startG = StartPay()
startG.start(wechat)
startG.start(alipay)

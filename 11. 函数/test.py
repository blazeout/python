"""
函数关键字 def :
"""
from typing import Optional, List


def hello(name, age):
    print("我的名字是:", name, "我的年龄是", age)
    print(type(name), print(age))


#  位置传参
hello("王嘉豪", 18)
#   指定传参
hello(age=18, name="wjh")


#  默认传参, age直接默认了不需要传入
def hello2(name, age=19):
    print(name, age)


#  默认传参需要改变就需要显示的指定出来
hello2("wjh", age=20)

hello2("wjh")


#  不定长传参, 其他的参数全部放到other元组, 不可修改~~
def hello3(name, *other):
    print(name, other)


hello3("王嘉豪", "睡觉", "听歌")


#  **other 指定传参, 变成字典~~
def hello4(name, **other):
    print(name, other)
    for key in other.keys():
        print(key)


hello4("wjh", teacher="tony", age=18)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#  内部函数
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = list()

    #  内部函数

    def dfs(root1):
        if root1 is None:
            return
        res.append(root1.val)
        dfs(root1.left)
        dfs(root1.right)

    dfs(root)
    return res

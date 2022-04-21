"""
往下走就是乘10, 往右走就是+1, 字典树
"""


class Solution:

    def lexicalOrder(self, n: int) -> [int]:
        res = []
        num = 1
        for i in range(n):
            res.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return res

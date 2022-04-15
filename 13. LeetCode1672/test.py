class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxRes = 0
        for i in range(len(accounts)):
            temp = 0
            for j in range(len(accounts[i])):
                temp += accounts[i][j]
            if temp > maxRes:
                maxRes = temp
        return maxRes


solution = Solution()
accounts = [[1, 5], [7, 3], [3, 5]]
ret = solution.maximumWealth(accounts)
print(ret)

#  一行代码
max(sum(accounts[i] for i in range(len(accounts))))



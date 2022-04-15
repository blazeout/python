class Solution:
    # 当我们遇到'1'的时候我们通过感染的方式将周围的岛屿全部感染为'0'

    def numIslands(self, grid: [[str]]) -> int:
        def dfs(i: int, j: int, grid: [[str]]):
            m, n = len(grid), len(grid[0])
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                dfs(x, y, grid)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j, grid)
                    ans += 1
        return ans

import bisect


class Solution:

    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(nums[i] + sums[i])
        for i in range(1, 1 + n):
            s = target + sums[i - 1]
            bound = bisect.bisect_left(sums, s)
            if bound <= n:
                ans = min(bound - i + 1, ans)

        return 0 if ans == n + 1 else ans


c = Solution()
c.minSubArrayLen(7, [2,3,1,2,4,3])

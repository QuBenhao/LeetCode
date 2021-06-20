import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, queries = test_input
        return self.minDifference(list(nums), [x[:] for x in queries])

    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # 差分数组
        diff = [[0] * 101]
        for num in nums:
            diff.append(list(diff[-1]))
            diff[-1][num] += 1

        ans = []
        for l, r in queries:
            res = 100  # 最大不会超过100
            last = -100
            # 我们通过差分数组求得l到r之间有哪些数
            for i in range(1, 101):
                if diff[r + 1][i] - diff[l][i] > 0:
                    res = min(res, i - last)
                    last = i
            ans.append(res if res < 100 else -1)
        return ans

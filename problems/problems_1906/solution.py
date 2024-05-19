import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minDifference(*test_input)

    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        m = max(nums)
        # 差分数组
        diff = [[0] * (m + 1)]
        for num in nums:
            diff.append(list(diff[-1]))
            diff[-1][num] += 1

        ans = []
        for l, r in queries:
            res = m  # 最大不会超过最大值
            last = -m  # 保证第一个数做差不影响结果
            # 我们通过差分数组求得l到r之间有哪些数
            for i in range(1, m + 1):
                if diff[r + 1][i] - diff[l][i] > 0:
                    res = min(res, i - last)
                    last = i
            ans.append(res if res < m else -1)
        return ans

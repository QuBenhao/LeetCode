import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, limit = test_input
        return self.minMoves(list(nums), limit)

    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        # 差分数组 d，范围是 [1, 2*limit+1]
        d = [0] * (limit * 2 + 2)
        # 记录 nums[i] + nums[n-i-1] 的频数
        freq = Counter()
        for i in range(n // 2):
            freq[nums[i] + nums[n - i - 1]] += 1
            # 对差分数组进行操作
            d[1 + min(nums[i], nums[n - i - 1])] += 1
            d[limit + max(nums[i], nums[n - i - 1]) + 1] -= 1

        ans = n * 2
        # 0/1 贡献的数量
        contrib01 = 0
        for K in range(2, limit * 2 + 1):
            contrib01 += d[K]
            # 通过哈希表查找 0 贡献的数量
            contrib1 = contrib01 - freq[K]
            contrib2 = n // 2 - contrib01
            ans = min(ans, contrib1 + contrib2 * 2)

        return ans

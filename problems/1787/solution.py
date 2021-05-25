import solution
from collections import Counter,defaultdict
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, k = test_input
        return self.minChanges(list(nums), k)

    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        counters = defaultdict(Counter)
        for i in range(k):
            for j in range(i, n, k):
                counters[i][nums[j]] += 1

        # 每组数的众数
        mcv = [counters[i].most_common(1)[0][1] for i in range(k)]
        # 每组全部变为同样的数的代价
        ans = n - sum(mcv)

        keys = [sorted(counters[i].keys(), key=lambda x: -counters[i][x]) for i in range(k)]

        # 每组数都是众数，要满足异或为0，需要统计每组数选哪个数达到最优解，或者牺牲哪组数
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == k and curr == 0:
                return 0
            elif idx == k:
                return float("inf")
            # 牺牲这组数的额外代价,所有数都换为某个数，使得异或为0
            res = mcv[idx]
            # 变为这组数中的某个数
            for key in keys[idx]:
                if mcv[idx] - counters[idx][key] >= res:
                    continue
                res = min(res, dfs(idx + 1, curr ^ key) - counters[idx][key] + mcv[idx])
            return res

        return ans + dfs(0, 0)
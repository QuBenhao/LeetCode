import solution
from collections import Counter,defaultdict
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minChanges(*test_input)

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

        # Mode of each group
        mcv = [counters[i].most_common(1)[0][1] for i in range(k)]
        # Cost to make each group uniform
        ans = n - sum(mcv)

        keys = [sorted(counters[i].keys(), key=lambda x: -counters[i][x]) for i in range(k)]

        # Starting from each group's mode, choose alternative values or sacrifice one group to achieve XOR 0 optimally
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == k and curr == 0:
                return 0
            elif idx == k:
                return float("inf")
            # Extra cost to sacrifice this group by changing all its values to make the XOR 0
            res = mcv[idx]
            # Change to a value already present in this group
            for key in keys[idx]:
                if mcv[idx] - counters[idx][key] >= res:
                    continue
                res = min(res, dfs(idx + 1, curr ^ key) - counters[idx][key] + mcv[idx])
            return res

        return ans + dfs(0, 0)

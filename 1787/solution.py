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
        # 按间隔为k分组
        counts = [Counter(nums[j] for j in range(i,n,k)) for i in range(k)]
        # 第一种情况：某一组数需要选择不在nums中的数。（如果有两组数要这样，可以一组选择nums中的数，另一组取异或值，故至多有一组数选不在nums中的数）
        # 每组数中出现最多的次数
        mcv = [counts[i].most_common(1)[0][1] for i in range(k)]
        # 我们要替换其中的一个，如果这个数不在nums中，那么最优必然是选择频次最少的那组数，这样变化最少
        # 除了每组出现频次最高的，其他全部换成该组频次最高的值，而有一个组要被全部替换，故不需要替换的数为sum(mcv)-min(mcv)个
        ans = n - sum(mcv) + min(mcv)

        # 第二种情况：所有组选取的数都在nums中。
        d = counts[0]
        for i in range(1, k):
            nd = defaultdict(int)
            for x in d:
                for y in counts[i]:
                    # 如果之前的异或结果为x，当前组中选择y，那么不用变的结果有d[x] + counts[i][y]个
                    nxt = x ^ y
                    # 尽可能地取多的数，这样需要的变化操作最少
                    nd[nxt] = max(nd[nxt], d[x] + counts[i][y])
            d = nd
        # 最终异或结果为0不需要变动的个数为d[0]
        return min(ans, n - d[0])

        # 第二种情况可以使用记忆化搜索或者dp
        # @lru_cache(None)
        # def f(idx, xor_val):
        #     if idx == 0:
        #         if xor_val in counts[idx]:
        #             return counts[idx][xor_val]
        #         else:
        #             return float("-inf")
        #     cur = 0
        #     for k,v in counts[idx].items():
        #         cur = max(cur, f(idx-1, xor_val ^ k) + v)
        #     return cur
        #
        # return min(ans, n - f(k-1, 0))

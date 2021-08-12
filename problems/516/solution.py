import solution
from functools import lru_cache
from collections import defaultdict
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestPalindromeSubseq(str(test_input))

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)

        n = len(s)
        # 预处理统计每个字母的所有坐标
        cIndex = defaultdict(list)
        for i, c in enumerate(s):
            cIndex[ord(c) - ord('a')].append(i)

        @lru_cache(None)
        def dfs(l, r):
            if l >= r:
                return 1 if l == r else 0
            ans = 0
            # 找处于区间l,r最左最右的a,b,c,d...,z
            for c in set(s[l:r + 1]):
                i = ord(c) - ord('a')
                left = bisect.bisect_left(cIndex[i], l)
                # 区间里没有这个字母
                if left == len(cIndex[i]):
                    continue
                right = bisect.bisect_left(cIndex[i], r)
                if right == len(cIndex[i]) or cIndex[i][right] > r:
                    right -= 1
                ans = max(ans, dfs(cIndex[i][left] + 1, cIndex[i][right] - 1) + 2) if right > left else max(ans, 1)
            return ans

        return dfs(0, n - 1)

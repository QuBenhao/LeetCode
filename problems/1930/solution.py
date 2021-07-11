import solution
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPalindromicSubsequence(str(test_input))

    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ans = defaultdict(set)
        # last_index = dict()
        # cnts = defaultdict(int)
        # for i, c in enumerate(s):
        #     if c in last_index and last_index[c] < i - 1:
        #         ans[c].update(set(s[last_index[c]+1:i]))
        #     last_index[c] = i
        #     cnts[c] += 1
        # return sum(len(v) for v in ans.values()) + sum(i > 2 for i in cnts.values())

        ans = 0
        for c in set(s):
            l = s.index(c)
            r = s.rindex(c)
            if l < r - 1:
                ans += len(set(s[l+1:r]))
        return ans

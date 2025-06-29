import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestCommonPrefix(test_input)

    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def get_cp(i, j):
            idx = 0
            while idx < len(words[i]) and idx < len(words[j]) and words[i][idx] == words[j][idx]:
                idx += 1
            return idx

        n = len(words)
        if n == 1:
            return [0]

        cps = [get_cp(i, i + 1) for i in range(n - 1)]
        suf_max = [0] * n
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], cps[i])
        pre_max = 0
        ans = [0] * n
        ans[0] = suf_max[1]
        for i in range(1, n - 1):
            ans[i] = max(pre_max, suf_max[i + 1], get_cp(i-1, i+1))
            pre_max = max(pre_max, cps[i - 1])
        ans[-1] = pre_max
        return ans

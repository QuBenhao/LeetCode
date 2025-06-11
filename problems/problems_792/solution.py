import solution
from typing import *
from collections import defaultdict
from bisect import bisect_right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numMatchingSubseq(*test_input)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        idx_map = defaultdict(list)
        for i, c in enumerate(s):
            idx_map[c].append(i)
        ans = 0
        for word in words:
            idx = 0
            s_idx = -1
            n = len(word)
            while idx < n:
                i = bisect_right(idx_map[word[idx]], s_idx)
                if i == len(idx_map[word[idx]]):
                    break
                s_idx = idx_map[word[idx]][i]
                idx += 1
            ans += idx == n
        return ans

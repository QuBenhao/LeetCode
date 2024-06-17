import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findLUSlength(test_input)

    def findLUSlength(self, strs: List[str]) -> int:
        def is_sub_seq(s: str, t: str) -> bool:
            ptr_s = ptr_t = 0
            while ptr_s < len(s) and ptr_t < len(t):
                if s[ptr_s] == t[ptr_t]:
                    ptr_s += 1
                ptr_t += 1
            return ptr_s == len(s)

        ans = -1
        for i, s in enumerate(strs):
            for j, t in enumerate(strs):
                if i != j and is_sub_seq(s, t):
                    break
            else:
                ans = max(ans, len(s))
        return ans

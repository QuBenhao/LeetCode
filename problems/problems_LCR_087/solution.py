import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.restoreIpAddresses(test_input)

    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment: str) -> bool:
            if segment[0] == '0' and len(segment) != 1:
                return False
            return int(segment) <= 255

        n = len(s)
        ans = []
        cur = []

        def backtrack(idx):
            if idx >= n or len(cur) > 3:
                return
            if len(cur) == 3:
                seg = s[idx:]
                if is_valid(seg):
                    ans.append('.'.join(cur + [seg]))
                return
            if s[idx] == "0":
                cur.append(s[idx])
                backtrack(idx + 1)
                cur.pop()
                return
            for i in range(idx, min(idx+3,n-3+len(cur))):
                seg = s[idx:i+1]
                if is_valid(seg):
                    cur.append(seg)
                    backtrack(i+1)
                    cur.pop()
        backtrack(0)
        return ans

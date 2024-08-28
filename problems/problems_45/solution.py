import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.jump(test_input)

    def jump(self, nums: List[int]) -> int:
        ans = 0
        cur, nxt = 0, 0
        while nxt < len(nums) - 1:
            ans += 1
            tmp = nxt
            for nx in range(cur, nxt + 1):
                tmp = max(tmp, nx + nums[nx])
            cur, nxt = nxt + 1, tmp
        return ans

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMatrix(test_input)

    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = {}
        ans = []
        for num in nums:
            if cnt.get(num, 0) == len(ans):
                ans.append([])
            ans[cnt.get(num, 0)].append(num)
            cnt[num] = cnt.get(num, 0) + 1
        return ans

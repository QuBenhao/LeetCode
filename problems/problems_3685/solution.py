import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subsequenceSumAfterCapping(*test_input)

    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        freq = [0] * (n + 1)
        for num in nums:
            freq[num] += 1
        used = 0
        ans = [False] * n
        dp = [False] * (k + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(freq[i]):
                for x in range(k, i - 1, -1):
                    dp[x] = dp[x] or dp[x - i]
            used += freq[i]
            for j in range(min(n - used, k//i) + 1):
                if dp[k - j * i]:
                    ans[i - 1] = True
                    break
        return ans

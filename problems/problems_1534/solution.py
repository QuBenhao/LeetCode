import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countGoodTriplets(*test_input)

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) > b or abs(arr[i] - arr[k]) > c:
                        continue
                    ans += 1
        return ans

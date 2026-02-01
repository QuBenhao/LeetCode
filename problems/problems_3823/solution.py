import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reverseByType(test_input)

    def reverseByType(self, s: str) -> str:
        arr = list(s)
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            while left < right and not arr[left].isalpha():
                left += 1
            while left < right and not arr[right].isalpha():
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        left, right = 0, n - 1
        while left < right:
            while left < right and arr[left].isalpha():
                left += 1
            while left < right and arr[right].isalpha():
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return "".join(arr)

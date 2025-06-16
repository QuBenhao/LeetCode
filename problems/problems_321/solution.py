from collections import deque
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxNumber(*test_input)

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_arr(arr: List[int], length: int) -> Deque[int]:
            stack = deque()
            drop = len(arr) - length
            for num in arr:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            for _ in range(len(stack) - length):
                stack.pop()
            return stack
        
        def merge(arr1: Deque[int], arr2: Deque[int]) -> List[int]:
            return [max(arr1, arr2).popleft() for _ in range(len(arr1) + len(arr2))]
        
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        max_combination = []
        for i in range(max(0, k - n), min(m, k) + 1):
            arr1 = pick_arr(nums1, i)
            arr2 = pick_arr(nums2, k - i)
            max_combination = max(max_combination, merge(arr1, arr2))
        return max_combination

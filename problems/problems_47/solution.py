import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.permuteUnique(test_input)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def next_permutation(arr):
            n = len(arr)
            i = n - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            left, right = i + 1, n - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            if i < 0:
                return
            j = i + 1
            while j < n and arr[j] <= arr[i]:
                j += 1
            arr[i], arr[j] = arr[j], arr[i]

        nums.sort()
        ans = [list(nums)]
        while True:
            next_permutation(nums)
            if nums == ans[0]:
                break
            ans.append(list(nums))
        return ans

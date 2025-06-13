import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.concatenatedDivisibility(*test_input)

    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums.sort()
        mod_nums = [num % k for num in nums]
        num = 0
        base = 0
        suf_length = [0] * n
        for i in range(n - 1, -1, -1):
            suf_length[i] = pow(10, base, k)
            num = (num + (mod_nums[i] * suf_length[i]) % k) % k
            base += len(str(nums[i]))
        
        def next_permutation():
            i = n - 2
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
            if i == -1:
                return False
            
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
            mod_nums[i], mod_nums[j] = mod_nums[j], mod_nums[i]

            l, r = i + 1, n - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                mod_nums[l], mod_nums[r] = mod_nums[r], mod_nums[l]
                l += 1
                r -= 1
            
            base = 0
            for idx in range(n-1, i-1, -1):
                suf_length[idx] = pow(10, base, k)
                base += len(str(nums[idx]))
            nonlocal num
            num = (num + ((mod_nums[i] - mod_nums[j]) % k * suf_length[i]) % k) % k
            num = (num - ((mod_nums[i] - mod_nums[j]) % k * suf_length[j]) % k + k) % k
            l, r = i + 1, n - 1
            while l < r:
                num = (num + ((mod_nums[l] - mod_nums[r]) * suf_length[l]) % k) % k
                num = (num - ((mod_nums[l] - mod_nums[r]) * suf_length[r]) % k + k) % k
                l += 1
                r -= 1
            return True

        while True:
            if num == 0:
                return nums
            
            if not next_permutation():
                return []

from functools import cache
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.concatenatedDivisibility(*test_input)

    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums.sort()
        pow10 = [10 ** len(str(num)) for num in nums]
        ans = []

        @cache
        def dfs(s, x) -> bool: # s 中二进制第i位为1表示nums[i]还未被使用, x是当前的余数
            if s == 0:
                return x == 0
            for i, (p10, num) in enumerate(zip(pow10, nums)): # 按顺序遍历, 优先将小的数放在前面
                if (s >> i) & 1 and dfs(s ^ (1 << i), (x * p10 + num) % k): # 在这里叠加前面的余数, 乘上当前的pow10相当于左移了
                    ans.append(num)
                    return True
            return False
        
        if dfs((1 << n) - 1, 0):
            return ans[::-1]
        return []

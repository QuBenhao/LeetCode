import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.permuteUnique(test_input)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(x):
            if x == len(nums) - 1:
                res.append(list(nums))  # 添加排列方案
                return
            dic = set()
            for i in range(x, len(nums)):
                if nums[i] in dic: continue  # 重复，因此剪枝
                dic.add(nums[i])
                nums[i], nums[x] = nums[x], nums[i]  # 交换，将 nums[i] 固定在第 x 位
                dfs(x + 1)  # 开启固定第 x + 1 位元素
                nums[i], nums[x] = nums[x], nums[i]  # 恢复交换

        res = []
        dfs(0)
        return res

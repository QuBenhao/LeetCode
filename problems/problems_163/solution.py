import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMissingRanges(*test_input)

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # ans = [[lower, upper]]
        # for num in nums:
        #     if ans[-1][0] < num:
        #         ans[-1][1] = num - 1
        #         ans.append([num + 1, upper])
        #     elif ans[-1][0] == num:
        #         ans[-1][0] += 1
        #     else:
        #         break
        #     if ans[-1][0] > ans[-1][1]:
        #         ans.pop()
        # return ans

        # 添加终止边界
        nums.append(upper + 1)
        ans = []
        last = lower - 1
        for num in nums:
            # 比上一个数字中有缺失,需要添加在答案中的
            if num - last > 2:
                ans.append([last + 1, num - 1])
            elif num - last == 2:
                ans.append([last + 1, last + 1])
            last = num
        return ans

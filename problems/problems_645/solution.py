import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findErrorNums(list(test_input))

    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # # 左边是重复的数，右边是丢失的数
        # return [Counter(nums).most_common(1)[0][0], (set(i for i in range(1, len(nums) + 1)) - set(nums)).pop()]

        # x = sum(nums) - sum(set(nums))
        # sum(nums) = x + 1 + ... + n - y
        # y = x + 1 + ... + n - sum(nums) = x + n * (n+1)//2 - sum(nums) = n * (n+1) // 2 - sum(set(nums))
        n, s = len(nums), sum(set(nums))
        return [sum(nums) - s, n * (n + 1) // 2 - s]

        # # 1 ^ 2 ^ ... ^ 4k = 4k
        # # 1 ^ 2 ^ ... ^ 4k+1 = 4k ^ 4k+1 = 1
        # # 1 ^ 2 ^ ... ^ 4k+2 = 4k+2 ^ 1 = 4k+3
        # # 1 ^ 2 ^ ... ^ 4k+3 = 0
        # n = len(nums)
        # # 应该的位运算结果
        # ans = [n, 1, n + 1, 0][n % 4]
        # # 实际的位运算结果以及重复的数字
        # res = repeat = 0
        # for num in nums:
        #     val = abs(num)
        #     res ^= val
        #     if nums[val - 1] < 0:
        #         repeat = val
        #     else:
        #         nums[val - 1] = -nums[val - 1]
        # # res的结果少异或了一次丢失的数, 多异或了一次重复的数，也就是说res^ans=x^y
        # return [repeat, repeat ^ res ^ ans]

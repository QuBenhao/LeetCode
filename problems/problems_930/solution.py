import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numSubarraysWithSum(*test_input)

    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        # countOnes = ans = 0
        # cnts = Counter({0:1})
        # for num in nums:
        #     if num:
        #         countOnes += 1
        #     ans += cnts[countOnes - goal]
        #     cnts[countOnes] += 1
        # return ans

        # 滑动窗口
        n = len(nums)
        ans = l1 = l2 = s1 = s2 = 0
        for r in range(n):
            s1 += nums[r]
            s2 += nums[r]
            while l1 <= r and s1 > goal:
                s1 -= nums[l1]
                l1 += 1
            while l2 <= r and s2 >= goal:
                s2 -= nums[l2]
                l2 += 1
            ans += l2 - l1
        return ans

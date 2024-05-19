import solution
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.triangleNumber(list(test_input))

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # nums.sort()
        # ans = 0
        # for i in range(n - 2):
        #     for j in range(i + 1, n - 1):
        #         idx = bisect.bisect_left(nums, nums[i] + nums[j])
        #         if idx > j:
        #             ans += idx - 1 - j
        # return ans

        n = len(nums)
        nums.sort()
        ans = 0
        # 固定最大边, a + b > c
        for i in range(n - 1, 1, -1):
            l, r = 0, i - 1
            # 两数之和问题！
            while l < r:
                # 两数之和大于最大边，他们之间的所有值作为左端点，均可以和右端点构成答案
                if nums[l] + nums[r] > nums[i]:
                    ans += r - l
                    r -= 1
                else:
                    # 小于最大边，构不成答案，之后的右端点都需要更大的左端点才有可能继续构成答案
                    l += 1
        return ans

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
        # Fix the largest side, a + b > c
        for i in range(n - 1, 1, -1):
            l, r = 0, i - 1
            # This is a two-sum problem!
            while l < r:
                # If the sum exceeds the largest side, every left endpoint between the pointers also works with this right endpoint
                if nums[l] + nums[r] > nums[i]:
                    ans += r - l
                    r -= 1
                else:
                    # If the sum is too small, later right endpoints need a larger left endpoint to form a valid triangle
                    l += 1
        return ans

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.singleNumber(test_input.copy())

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # slow = fast = 0
        # nums.sort()
        # while fast < n:
        #     fast += 1
        #     if fast >= n:
        #         break
        #     if nums[slow] == nums[fast]:
        #         slow = fast = fast + 1
        #     else:
        #         return nums[slow]
        # return nums[slow]

        # Each element that occurs twice XORs to 0, so XORing all elements leaves the single element
        ans = 0
        for num in nums:
            ans ^= num
        return ans

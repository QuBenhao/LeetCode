import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumUniqueSubarray(test_input.copy())

    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = cur = left = 0
        seen = set()
        for num in nums:
            while num in seen:
                cur -= nums[left]
                seen.remove(nums[left])
                left += 1
            cur += num
            ans = max(ans, cur)
            seen.add(num)
        return ans

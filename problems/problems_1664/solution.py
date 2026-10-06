import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.waysToMakeFair(list(test_input))

    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Difference between the even-index and odd-index sums
        delta = sum(nums[0::2]) - sum(nums[1::2])
        # Sign
        flag = 1
        res = 0
        # Current sum
        cur = 0
        for i, num in enumerate(nums):
            # Subtract twice the preceding sum to flip its signs: added even values become subtractions, and subtracted odd values become additions
            if delta - 2 * cur - flag * num == 0:
                res += 1
            cur += flag * num
            flag *= -1
        return res


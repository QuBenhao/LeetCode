import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkSubarraySum(*test_input)

    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        modes = set()
        presum = 0
        for num in nums:
            temp = presum
            # Current prefix sum
            presum += num
            presum %= k
            # Modular congruence
            if presum in modes:
                return True
            # The previous prefix sum can be used on the next iteration, when it is two positions away
            modes.add(temp)
        return False

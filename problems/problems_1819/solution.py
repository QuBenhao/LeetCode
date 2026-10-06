import solution
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countDifferentSubsequenceGCDs(list(test_input))

    def countDifferentSubsequenceGCDs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # For x to be a sequence's GCD, every number in the sequence must be a multiple of x
        ans = 0
        nums = set(nums)
        c = max(nums)
        # A subsequence's GCD must lie between 1 and the maximum value
        for i in range(1, c+1):
            g = None
            # Check whether such a sequence exists by starting at i and stepping by i
            for j in range(i, c+1, i):
                # j is in nums; try including it
                if j in nums:
                    if not g:
                        g = j
                    else:
                        g = math.gcd(j, g)
                    # At least two numbers in nums have GCD i
                    if g == i:
                        ans += 1
                        break
        return ans

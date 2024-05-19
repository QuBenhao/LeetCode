import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(list(test_input))

    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, ans = 0, 0
        for n in nums:
            if n <= last:
                ans += last + 1 - n
                last += 1
            else:
                last = n
        return ans

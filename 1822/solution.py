import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.arraySign(list(test_input))

    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums:
            return 0
        count = 0
        for n in nums:
            if n < 0:
                count += 1
        return 1 if count % 2 == 0 else -1

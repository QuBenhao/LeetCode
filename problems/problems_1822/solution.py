import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.arraySign(list(test_input))

    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for num in nums:
            if not num:
                return 0
            if num < 0:
                cnt += 1
        return -1 if cnt % 2 else 1

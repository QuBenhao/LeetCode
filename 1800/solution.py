import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxAscendingSum(list(test_input))

    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        last,s = None, 0
        for n in nums:
            if last is not None:
                if n > last:
                    s += n
                else:
                    ans = max(ans, s)
                    s = n
            else:
                s = n
            last = n
        return max(ans, s)

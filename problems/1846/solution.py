import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumElementAfterDecrementingAndRearranging(list(test_input))

    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        limit = 1
        for num in arr[1:]:
            limit = min(limit + 1, num)
        return limit

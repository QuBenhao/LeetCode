import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumElementAfterDecrementingAndRearranging(list(test_input))

    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        cnts = [0] * (n + 1)
        for num in arr:
            cnts[min(num, n)] += 1
        ans = 0
        for i in range(1, n + 1):
            ans = min(i, ans + cnts[i])
        return ans

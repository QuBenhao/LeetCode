import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.hIndex(list(test_input))

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l, r = 0, n
        while l < r:
            mid = l + r + 1 >> 1
            if citations[n - mid] >= mid:
                l = mid
            else:
                r = mid - 1
        return l

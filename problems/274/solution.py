import solution
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.hIndex(list(test_input))

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # # h-index (f) = max(i -> f(i) >= i)
        # for i,j in enumerate(sorted(citations, reverse=True), 1):
        #     if j < i:
        #         return i - 1
        # return len(citations)

        n = len(citations)
        citations.sort(reverse=True)
        l, r = 0, n
        while l < r:
            mid = l + r + 1 >> 1
            if citations[mid - 1] >= mid:
                l = mid
            else:
                r = mid - 1
        return l

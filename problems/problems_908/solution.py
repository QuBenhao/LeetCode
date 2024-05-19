import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestRangeI(*test_input)

    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0, max(A) - min(A) - 2 * K)
        # n = len(A)
        # average = (max(A)+min(A))/2
        # for i in range(n):
        #     if A[i] - average >= K:
        #         A[i] -= K
        #     elif average - A[i] >= K:
        #         A[i] += K
        #     else:
        #         A[i] = average
        # return max(A) - min(A)

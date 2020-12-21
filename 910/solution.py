import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        A, K = test_input
        return self.smallestRangeII(A.copy(), K)

    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        curr_max = A[-1]
        smallest = curr_max-A[0]
        n = len(A)
        for i in range(n - 1):
            new = A[i] + 2 * K
            curr_max = max(new, curr_max)
            curr_min = min(A[i+1], A[0] + 2*K)
            smallest = min(smallest, curr_max - curr_min)
        return smallest

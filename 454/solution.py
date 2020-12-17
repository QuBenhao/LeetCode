import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        A, B, C, D = test_input
        return self.fourSumCount(A.copy(),B.copy(),C.copy(),D.copy())

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        import collections
        ab = collections.Counter()
        cd = collections.Counter()
        target = 0
        n = len(A)
        for i in range(n):
            for j in range(n):
                ab[A[i]+B[j]] += 1
                cd[C[i]+D[j]] += 1
        count = 0
        for k in ab.keys():
            count += ab[k] * cd[target-k]
        return count

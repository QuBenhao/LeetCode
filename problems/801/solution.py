import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSwap(*test_input)

    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n, s = 0, 0
        if A[0] != B[0]:
            s = 1

        for i in range(1, len(A)):
            ts, tn = s, n
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                ts = s + 1
            else:
                ts = n + 1
                tn = s
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                tn = min(tn, s)
                ts = min(ts, n + 1)
            n, s = tn, ts

        return min(n, s)

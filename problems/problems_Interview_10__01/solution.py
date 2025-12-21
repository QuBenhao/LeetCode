import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        A, m, B, n = test_input
        self.merge(A, m, B, n)
        return A

    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        i, j, idx = m - 1, n - 1, m + n - 1
        while idx >= 0:
            if i >= 0 and j >= 0:
                if A[i] < B[j]:
                    A[idx] = B[j]
                    j -= 1
                else:
                    A[idx] = A[i]
                    i -= 1
            elif i >= 0:
                A[idx] = A[i]
                i -= 1
            else:
                A[idx] = B[j]
                j -= 1
            idx -= 1

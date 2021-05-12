import solution
from itertools import accumulate
from operator import xor


class Solution(solution.Solution):
    def solve(self, test_input=None):
        arr, queries = test_input
        return self.xorQueries(list(arr), [x[:] for x in queries])

    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prexor = list(accumulate([0] + arr, xor))
        return [prexor[i] ^ prexor[j + 1] for i, j in queries]

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        mat, k = test_input
        return self.kWeakestRows([x[:] for x in mat], k)

    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        return [x[0] for x in sorted(enumerate(mat), key=lambda x:sum(x[1]))][:k]

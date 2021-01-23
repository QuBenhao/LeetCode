import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.diagonalSort([x[:] for x in test_input])

    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        import collections
        diags = collections.defaultdict(list)
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                diags[i-j].append(mat[i][j])
        for v in diags.values():
            v.sort()
        for i in range(m):
            for j in range(n):
                mat[i][j] = diags[i-j].pop(0)
        return mat

        # import collections, heapq
        # diags = collections.defaultdict(list)
        # m = len(mat)
        # n = len(mat[0])
        # for i in range(m):
        #     for j in range(n):
        #         heapq.heappush(diags[i-j], mat[i][j])
        # for i in range(m):
        #     for j in range(n):
        #         mat[i][j] = heapq.heappop(diags[i-j])
        # return mat

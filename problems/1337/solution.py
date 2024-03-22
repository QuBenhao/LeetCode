import solution
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.kWeakestRows(*test_input)

    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # return [x[0] for x in sorted(enumerate(mat), key=lambda x:sum(x[1]))[:k]]

        m, n = len(mat), len(mat[0])
        q = []
        for i in range(m):
            l, r = 0, n - 1
            while l < r:
                mid = l + r + 1 >> 1
                if mat[i][mid]:
                    l = mid
                else:
                    r = mid - 1
            cur = r + 1 if mat[i][r] else r
            if len(q) == k and -q[0][0] > cur:
                heapq.heappop(q)
            if len(q) < k:
                heapq.heappush(q, (-cur, -i))
        ans = [0] * k
        idx = k - 1
        while q:
            ans[idx] = -heapq.heappop(q)[1]
            idx -= 1
        return ans

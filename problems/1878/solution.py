import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getBiggestThree([x[:] for x in test_input])

    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        val = set()

        psum1 = [[0] * (m + 1) for _ in range(m + n)]
        psum2 = [[0] * (m + 1) for _ in range(m + n)]

        for k in range(m + n):
            for i in range(m):
                j = k - i
                if 0 <= j < n:
                    psum1[k][i + 1] = psum1[k][i] + grid[i][j]
                j = k + i - (m - 1)
                if 0 <= j < n:
                    psum2[k][i + 1] = psum2[k][i] + grid[i][j]

        for i in range(m):
            for j in range(n):
                val.add(grid[i][j])
                for k in range(1, m):
                    if 0 <= i + 2 * k < m and 0 <= j - k < n and 0 <= j + k < n:
                        tmp = 0
                        idx1 = i + j
                        idx2 = i + j + 2 * k
                        idx3 = j - i + (m - 1)
                        idx4 = j - i + (m - 1) - 2 * k
                        tmp += psum1[idx1][i + k + 1] - psum1[idx1][i + 1] + psum1[idx2][i + 2 * k] - psum1[idx2][i + k]
                        tmp += psum2[idx3][i + k] - psum2[idx3][i] + psum2[idx4][i + 2 * k + 1] - psum2[idx4][i + k + 1]
                        val.add(tmp)
                    else:
                        break
        val = sorted(val)[::-1]
        return val[:3]

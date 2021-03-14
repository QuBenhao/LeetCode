import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, m, broken = test_input
        return self.domino(n, m, broken)

    def domino(self, n, m, broken):
        """
        :type n: int
        :type m: int
        :type broken: List[List[int]]
        :rtype: int
        """
        def neighbors(i, j):
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < n and 0 <= nj < m:
                    yield ni, nj

        def dfs(i, j, visited):
            print(match, visited)
            visited.add((i, j))
            for ni, nj in neighbors(i, j):
                nxt = match[ni][nj]
                if nxt in visited:
                    continue
                if not nxt or dfs(*nxt, visited):
                    match[i][j] = (ni, nj)
                    match[ni][nj] = (i, j)
                    return True
            return False

        match = [[None] * m for _ in range(n)]
        for i, j in broken:
            match[i][j] = '#'
        return sum(
            dfs(i, j, {'#'})
            for i in range(n)
            for j in range(m)
            if match[i][j] != '#' and (i + j) % 2  # 考虑奇数结点为起点
        )

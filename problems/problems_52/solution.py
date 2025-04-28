import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.totalNQueens(test_input)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # queens[i] means the column position for queen at i-1 th row
        # lu_rd: left up corner to right down corner
        # ld_ru: left down corner to right up corner
        def dfs(queens, lu_rd, ld_ru):
            row = len(queens)
            if row == n:
                nonlocal ans
                ans += 1
                return
            for col in range(n):
                if col not in queens and col - row not in lu_rd and row + col not in ld_ru:
                    queens.add(col)
                    lu_rd.add(col - row)
                    ld_ru.add(row + col)
                    dfs(queens, lu_rd, ld_ru)
                    queens.remove(col)
                    lu_rd.remove(col - row)
                    ld_ru.remove(row + col)

        ans = 0
        dfs(set(), set(), set())
        return ans

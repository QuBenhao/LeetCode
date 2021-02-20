import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.solveNQueens(test_input)

    def solveNQueens(self, n):
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
                ans.append(queens)
                return
            for col in range(n):
                if col not in queens and col - row not in lu_rd and row + col not in ld_ru:
                    dfs(queens+[col],lu_rd+[col - row],ld_ru+[row + col])

        ans = []
        dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (n-i-1) for i in res] for res in ans]

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.gameOfLife([x[:] for x in test_input])

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        board_ = [x[:] for x in board]

        for i in range(m):
            for j in range(n):
                count = sum([board_[r][c] for r in range(i - 1, i + 2) for c in range(j - 1, j + 2) if
                             0 <= r < m and 0 <= c < n]) - board_[i][j]
                if board_[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = 0
                elif board_[i][j] == 0 and count == 3:
                    board[i][j] = 1

        return board

    # infinite solution

    # def gameOfLifeInfinite(self, live):
    #     import collections
    #     ctr = collections.Counter((I, J)
    #                               for i, j in live
    #                               for I in range(i-1, i+2)
    #                               for J in range(j-1, j+2)
    #                               if I != i or J != j)
    #     return {ij
    #             for ij in ctr
    #             if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}
    #
    # def gameOfLife(self, board):
    #     live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
    #     live = self.gameOfLifeInfinite(live)
    #     for i, row in enumerate(board):
    #         for j in range(len(row)):
    #             row[j] = int((i, j) in live)

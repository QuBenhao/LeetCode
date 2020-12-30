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

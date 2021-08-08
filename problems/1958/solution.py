import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        board, rMove, cMove, color = test_input
        return self.checkMove([x[:] for x in board], rMove, cMove, str(color))

    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """

        def check(x, y):
            if color == 'W':
                other = 'B'
            else:
                other = 'W'
            length = 0
            if x == rMove:
                if y > cMove:
                    for i in range(cMove + 1, y):
                        if board[x][i] != other:
                            return False
                        length += 1
                else:
                    for i in range(y + 1, cMove):
                        if board[x][i] != other:
                            return False
                        length += 1
            elif y == cMove:
                if x > rMove:
                    for i in range(rMove + 1, x):
                        if board[i][y] != other:
                            return False
                        length += 1
                else:
                    for i in range(x + 1, rMove):
                        if board[i][y] != other:
                            return False
                        length += 1
            elif abs(rMove - x) == abs(cMove - y):
                if rMove - x == cMove - y:
                    if rMove > x:
                        j = y + 1
                        for i in range(x + 1, rMove):
                            if board[i][j] != other:
                                return False
                            j += 1
                            length += 1
                    else:
                        j = cMove + 1
                        for i in range(rMove + 1, x):
                            if board[i][j] != other:
                                return False
                            j += 1
                            length += 1
                else:
                    if rMove > x:
                        j = y - 1
                        for i in range(x + 1, rMove):
                            if board[i][j] != other:
                                return False
                            j -= 1
                            length += 1
                    else:
                        j = cMove - 1
                        for i in range(rMove + 1, x):
                            if board[i][j] != other:
                                return False
                            j -= 1
                            length += 1
            return True if length else False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == color:
                    if check(i, j):
                        return True
        return False

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isValidSudoku(test_input)

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)
        box = int(n ** 0.5)

        def valid():
            for i in range(n):
                nums_r = []
                nums_c = []
                nums_b = []
                for j in range(n):
                    box_r = i // box * box + j // box
                    box_c = i % box * box + j % box
                    if board[i][j] != '.':
                        if board[i][j] in nums_r:
                            return False
                        nums_r.append(board[i][j])
                    if board[j][i] != '.':
                        if board[j][i] in nums_c:
                            return False
                        nums_c.append(board[j][i])
                    if board[box_r][box_c] != '.':
                        if board[box_r][box_c] in nums_b:
                            return False
                        nums_b.append(board[box_r][box_c])
            return True

        return valid()

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.solveSudoku(test_input)

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # def valid(val, row, col):
        #     for c in range(len(board)):
        #         if c == col:
        #             continue
        #         if board[row][c] == str(val):
        #             return False
        #
        #     for r in range(len(board)):
        #         if r == row:
        #             continue
        #         if board[r][col] == str(val):
        #             return False
        #
        #     box = int(len(board) ** 0.5)
        #     rbox = int(row/box)
        #     cbox = int(col/box)
        #     for r in range(rbox * box, (rbox+1)*box):
        #         for c in range(cbox * box, (cbox+1)*box):
        #             if r == row and c== col:
        #                 continue
        #             if board[r][c] == str(val):
        #                 return False
        #     return True
        #
        # def backtracking(row, col):
        #     if col == len(board):
        #         return backtracking(row + 1, 0)
        #     if row == len(board):
        #         return True
        #     if board[row][col] == '.':
        #         for val in range(1, len(board) + 1):
        #             if valid(val, row, col):
        #                 board[row][col] = str(val)
        #                 if backtracking(row, col + 1):
        #                     return True
        #                 else:
        #                     board[row][col] = '.'
        #     else:
        #         return backtracking(row, col + 1)
        #     return False
        #
        # backtracking(0, 0)
        # return board

        """ 
        Solving an exact cover problem. 
        The following nondeterministic algorithm, which I will call algorithm X for lack of a better name, 
        finds all solutions to the exact cover problem defined by any given matrix A of 0s and 1s. 
        Algorithm X is simply a statement of the obvious trial-and-error approach. 
        (Indeed, I can’t think of any other reasonable way to do the job, in general.) 
        
        If A is empty, the problem is solved; terminate successfully. 
        Otherwise choose a column, c (deterministically). 
        Choose a row, r, such that A[r, c] = 1 (nondeterministically). 
        Include r in the partial solution. 
        For each j such that A[r, j] = 1, delete column j from matrix A; 
        for each i such that A[i, j] = 1, delete row i from matrix A. 
        Repeat this algorithm recursively on the reduced matrix A. 
        """

        header_dict = dict()
        h = ColumnNode()
        size = len(board)
        solution = []

        def rowRange(cIndex):
            rows = [0] * size
            res = int(cIndex / size ** 2)
            if res == 0:
                column = cIndex % size
                row = int(cIndex / size)
                for i in range(0, size):
                    rows[i] = row * size ** 2 + column * size + i
            elif res == 1:
                cIndex -= size ** 2
                row = int(cIndex / size)
                valueIndex = cIndex % size
                for c in range(0, size):
                    rows[c] = row * size ** 2 + c * size + valueIndex
            elif res == 2:
                cIndex = cIndex - size ** 2 * 2
                column = int(cIndex / size)
                valueIndex = cIndex % size
                for r in range(0, size):
                    rows[r] = r * size ** 2 + column * size + valueIndex
            else:
                cIndex = cIndex - size ** 2 * 3
                valueIndex = cIndex % size
                box = int(cIndex / size)
                boxsize = int(size ** 0.5)
                for r in range(int(box / boxsize) * boxsize, (int(box / boxsize) + 1) * boxsize):
                    for c in range(box % boxsize * boxsize, (box % boxsize + 1) * boxsize):
                        rows[(r - int(box / boxsize) * boxsize) * boxsize + (
                                c - box % boxsize * boxsize)] = r * size ** 2 + c * size + valueIndex
            return rows

        def columnRange(rIndex):
            columns = [0] * 4
            row = int(rIndex / size ** 2)
            column = int(rIndex % (size ** 2) / len(board))
            valueIndex = int((rIndex % size ** 2) % len(board))
            columns[0] = row * size + column
            columns[1] = size ** 2 + row * size + valueIndex
            columns[2] = size ** 2 * 2 + column * size + valueIndex
            columns[3] = size ** 2 * 3 + (
                        int(int(row / size ** 0.5) * size ** 0.5) + int(column / size ** 0.5)) * size + valueIndex
            return columns

        def findMinColumn():
            t = h.R
            min = h
            m = size + 1
            while t != h:
                if t.S == 0:
                    min = h
                    break
                if t.S < m:
                    m = t.S
                    min = t
                t = t.R
            return min

        def findNode(c, rIndex, cIndex):
            node = c.D
            for i in range(0, size):
                if (rowRange(cIndex)[i] == rIndex):
                    break
                node = node.D
            return node

        def cover(c):
            c.removeH()
            i = c.D
            while i != c:
                j = i.R
                while j != i:
                    j.removeV()
                    j = j.R
                i = i.D

        def uncover(c):
            i = c.U
            while i != c:
                j = i.L
                while j != i:
                    j.addV()
                    j = j.L
                i = i.U
            c.addH()

        def solving():
            if h.R == h:
                for i in solution:
                    while i.c.N >= size ** 2:
                        i = i.L
                    row = int(i.c.N / size)
                    column = i.c.N % size
                    valueIndex = i.R.c.N - size ** 2 - row * size
                    board[row][column] = str(valueIndex + 1)
                return True
            c = findMinColumn()
            if c == h: return False
            r = c.D
            cover(c)
            while r != c:
                solution.append(r)
                j = r.R
                while j != r:
                    cover(j.c)
                    j = j.R

                if solving(): return True
                solution.remove(r)
                j = r.L
                while j != r:
                    uncover(j.c)
                    j = j.L
                r = r.D
            uncover(c)
            return False

        for i in range(0, len(board) ** 2 * 4):
            c = ColumnNode(i)
            header_dict[i] = c
            for j in range(0, len(board)):
                node = DancingNode(c)
                c.linkDown(node)
                if j == 0:
                    node.D = c
                    c.U = node
            if i == 0:
                h.linkRight(c)
            else:
                header_dict[i - 1].linkRight(c)
            if i == len(board) ** 2 * 4 - 1:
                c.R = h
                h.L = c

        for i in range(0, size ** 2):
            for j in range(0, size):
                rIndex = rowRange(i)[j]

                r = findNode(header_dict.get(columnRange(rIndex)[0]), rIndex, columnRange(rIndex)[0])
                for k in range(3, 0, -1):
                    c = findNode(header_dict.get(columnRange(rIndex)[k]), rIndex, columnRange(rIndex)[k])
                    r.linkRight(c)
                    if k == 3:
                        r.L = c
                        c.R = r

        for r in range(0, size):
            for c in range(0, size):
                if board[r][c] != ".":
                    val = int(board[r][c])
                    val -= 1
                    rIndex = r * size ** 2 + c * size + val
                    for k in range(0, 4):
                        cover(header_dict[columnRange(rIndex)[k]])

        solving()
        return board


class DancingNode:
    def __init__(self, c=None):
        self.U = self.D = self.L = self.R = self
        self.c = c

    def linkRight(self, node):
        node.L = self
        node.R = self.R
        self.R.L = node
        self.R = node

    def linkDown(self, node):
        node.U = self
        self.D.U = node
        node.D = self.D
        self.D = node
        self.c.S += 1

    def removeH(self):
        self.L.R = self.R
        self.R.L = self.L

    def removeV(self):
        self.U.D = self.D
        self.D.U = self.U
        self.c.S -= 1

    def addH(self):
        self.L.R = self
        self.R.L = self

    def addV(self):
        self.U.D = self
        self.D.U = self
        self.c.S += 1


class ColumnNode(DancingNode):
    def __init__(self, N=None):
        super().__init__(self)
        # size
        self.S = 0
        # name
        self.N = N

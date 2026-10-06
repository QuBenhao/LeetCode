import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countCombinations(*test_input)

    # Compute all legal moves for the piece at (x0,y0) in directions dirs
    def generate_moves(self, x0: int, y0: int, dirs: List[Tuple[int, int]]) -> List[Tuple[int, int, int, int, int]]:
        SIZE = 8
        moves = [(x0, y0, 0, 0, 0)]  # Stay in place
        for dx, dy in dirs:
            # Move 1,2,3,... steps in direction (dx,dy)
            x, y = x0 + dx, y0 + dy
            step = 1
            while 0 < x <= SIZE and 0 < y <= SIZE:
                moves.append((x0, y0, dx, dy, step))
                x += dx
                y += dy
                step += 1
        return moves

    # Check that two moves are compatible: the pieces never overlap at the same time
    def is_valid(self, move1: Tuple[int, int, int, int, int], move2: Tuple[int, int, int, int, int]) -> bool:
        x1, y1, dx1, dy1, step1 = move1
        x2, y2, dx2, dy2, step2 = move2
        for i in range(max(step1, step2)):
            # Take one step per second
            if i < step1:
                x1 += dx1
                y1 += dy1
            if i < step2:
                x2 += dx2
                y2 += dy2
            if x1 == x2 and y1 == y2:  # Overlap
                return False
        return True

    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        rook_dirs = (-1, 0), (1, 0), (0, -1), (0, 1)  # Up, down, left, and right
        bishop_dirs = (1, 1), (-1, 1), (-1, -1), (1, -1)  # Diagonals
        piece_dirs = {'r': rook_dirs, 'b': bishop_dirs, 'q': rook_dirs + bishop_dirs}
        # Precompute all legal moves
        all_moves = [self.generate_moves(x, y, piece_dirs[piece[0]])
                     for piece, (x, y) in zip(pieces, positions)]

        n = len(pieces)
        path = [None] * n  # The length of path is fixed
        ans = 0
        def dfs(i: int) -> None:
            if i == n:
                nonlocal ans
                ans += 1
                return
            # Enumerate all legal moves for the current piece
            for move1 in all_moves[i]:
                # Check whether the legal move move1 is compatible
                if all(self.is_valid(move1, move2) for move2 in path[:i]):
                    path[i] = move1  # Overwrite directly; no state restoration is needed
                    dfs(i + 1)  # Enumerate all combinations of legal moves for the remaining pieces
        dfs(0)
        return ans

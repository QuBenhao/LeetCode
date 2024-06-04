import solution
from typing import *
from itertools import combinations


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.tictactoe(test_input)

    def tictactoe(self, moves: List[List[int]]) -> str:
        def in_a_row(points: List[List[int]]) -> bool:
            rows, cols = zip(*points)
            if rows.count(rows[0]) == len(rows):
                return True
            if cols.count(cols[0]) == len(cols):
                return True
            if all(x == y for x, y in points):
                return True
            if all(x + y == 2 for x, y in points):
                return True
            return False

        moves_a, moves_b = [], []
        for i, move in enumerate(moves):
            if i % 2:
                moves_b.append(move)
            else:
                moves_a.append(move)
        for a, b, c in combinations(moves_a, 3):
            if in_a_row([a, b, c]):
                return "A"
        for a, b, c in combinations(moves_b, 3):
            if in_a_row([a, b, c]):
                return "B"
        return "Draw" if len(moves) == 9 else "Pending"

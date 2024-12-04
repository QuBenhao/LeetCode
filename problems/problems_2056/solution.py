import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countCombinations(*test_input)

    # 计算位于 (x0,y0) 的棋子在 dirs 这些方向上的所有合法移动
    def generate_moves(self, x0: int, y0: int, dirs: List[Tuple[int, int]]) -> List[Tuple[int, int, int, int, int]]:
        SIZE = 8
        moves = [(x0, y0, 0, 0, 0)]  # 原地不动
        for dx, dy in dirs:
            # 往 (dx,dy) 方向走 1,2,3,... 步
            x, y = x0 + dx, y0 + dy
            step = 1
            while 0 < x <= SIZE and 0 < y <= SIZE:
                moves.append((x0, y0, dx, dy, step))
                x += dx
                y += dy
                step += 1
        return moves

    # 判断两个移动是否合法，即不存在同一时刻两个棋子重叠的情况
    def is_valid(self, move1: Tuple[int, int, int, int, int], move2: Tuple[int, int, int, int, int]) -> bool:
        x1, y1, dx1, dy1, step1 = move1
        x2, y2, dx2, dy2, step2 = move2
        for i in range(max(step1, step2)):
            # 每一秒走一步
            if i < step1:
                x1 += dx1
                y1 += dy1
            if i < step2:
                x2 += dx2
                y2 += dy2
            if x1 == x2 and y1 == y2:  # 重叠
                return False
        return True

    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        rook_dirs = (-1, 0), (1, 0), (0, -1), (0, 1)  # 上下左右
        bishop_dirs = (1, 1), (-1, 1), (-1, -1), (1, -1)  # 斜向
        piece_dirs = {'r': rook_dirs, 'b': bishop_dirs, 'q': rook_dirs + bishop_dirs}
        # 预处理所有合法移动
        all_moves = [self.generate_moves(x, y, piece_dirs[piece[0]])
                     for piece, (x, y) in zip(pieces, positions)]

        n = len(pieces)
        path = [None] * n  # 注意 path 的长度是固定的
        ans = 0
        def dfs(i: int) -> None:
            if i == n:
                nonlocal ans
                ans += 1
                return
            # 枚举当前棋子的所有合法移动
            for move1 in all_moves[i]:
                # 判断合法移动 move1 是否有效
                if all(self.is_valid(move1, move2) for move2 in path[:i]):
                    path[i] = move1  # 直接覆盖，无需恢复现场
                    dfs(i + 1)  # 枚举后续棋子的所有合法移动组合
        dfs(0)
        return ans

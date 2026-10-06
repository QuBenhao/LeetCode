from collections import deque
from typing import List, Tuple

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canMouseWin(*test_input)

    # 913. Cat and Mouse
    def catMouseGame(self, g_mouse: List[List[int]], g_cat: List[List[int]], mouse_start: int, cat_start: int,
                     hole: int) -> int:
        n = len(g_mouse)
        deg = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                deg[i][j][0] = len(g_mouse[i])
                deg[i][j][1] = len(g_cat[j])

        winner = [[[0, 0] for _ in range(n)] for _ in range(n)]
        q = deque()
        for i in range(n):
            winner[hole][i][1] = 1  # The mouse reaches the hole (the cat moves next): the mouse wins
            winner[i][hole][0] = 2  # The cat reaches the hole (the mouse moves next): the cat wins
            winner[i][i][0] = winner[i][i][1] = 2  # The cat and mouse occupy the same node: the cat wins regardless of whose turn it is
            q.append((hole, i, 1))
            q.append((i, hole, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))

        # Get unresolved predecessor states of (mouse, cat, turn)
        def get_pre_states() -> List[Tuple[int, int]]:
            if turn:  # It is the cat's turn; enumerate the mouse's previous positions
                return [(pre_mouse, cat) for pre_mouse in g_mouse[mouse] if winner[pre_mouse][cat][0] == 0]
            # It is the mouse's turn; enumerate the cat's previous positions
            return [(mouse, pre_cat) for pre_cat in g_cat[cat] if winner[mouse][pre_cat][1] == 0]

        # Decrease the predecessor state's degree
        def dec_deg_to_zero() -> bool:
            deg[pre_mouse][pre_cat][pre_turn] -= 1
            return deg[pre_mouse][pre_cat][pre_turn] == 0

        while q:
            mouse, cat, turn = q.popleft()
            win = winner[mouse][cat][turn]  # Eventual winner
            pre_turn = turn ^ 1
            for pre_mouse, pre_cat in get_pre_states():
                # Case 1: the mouse moved from pre to cur and eventually wins; mark pre with winner = mouse
                # Case 2: the cat moved from pre to cur and eventually wins; mark pre with winner = cat
                # Case 3: the mouse moved from pre to cur and the cat wins; leave pre unresolved until all its successors are cat wins, then mark winner = cat
                # Case 4: the cat moved from pre to cur and the mouse wins; leave pre unresolved until all its successors are mouse wins, then mark winner = mouse
                if pre_turn == win - 1 or dec_deg_to_zero():
                    winner[pre_mouse][pre_cat][pre_turn] = win
                    q.append((pre_mouse, pre_cat, pre_turn))

        # The mouse starts at mouse_start, the cat at cat_start, and the mouse moves first
        return winner[mouse_start][cat_start][0]  # Return the eventual winner (or a draw)

    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        DIRS = (0, -1), (0, 1), (-1, 0), (1, 0)  # Left, right, up, down
        m, n = len(grid), len(grid[0])
        # Build separate graphs for the mouse and cat
        g_mouse = [[] for _ in range(m * n)]
        g_cat = [[] for _ in range(m * n)]
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == '#':  # Wall
                    continue
                if c == 'M':  # Mouse position
                    mx, my = i, j
                elif c == 'C':  # Cat position
                    cx, cy = i, j
                elif c == 'F':  # Food (hole) position
                    fx, fy = i, j
                v = i * n + j  # Map 2D coordinates (i,j) to 1D coordinate v
                for dx, dy in DIRS:  # Enumerate the four directions: left, right, up, down
                    for k in range(mouseJump + 1):  # Enumerate jump lengths
                        x, y = i + k * dx, j + k * dy
                        if not (0 <= x < m and 0 <= y < n and grid[x][y] != '#'):  # Out of bounds or blocked by a wall
                            break
                        g_mouse[v].append(x * n + y)  # Add an edge
                    for k in range(catJump + 1):  # Enumerate jump lengths
                        x, y = i + k * dx, j + k * dy
                        if not (0 <= x < m and 0 <= y < n and grid[x][y] != '#'):  # Out of bounds or blocked by a wall
                            break
                        g_cat[v].append(x * n + y)  # Add an edge

        # Check whether the mouse wins
        return self.catMouseGame(g_mouse, g_cat, mx * n + my, cx * n + cy, fx * n + fy) == 1

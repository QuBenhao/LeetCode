import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        grid, catJump, mouseJump = test_input
        return self.canMouseWin(list(grid), catJump, mouseJump)

    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        mx = my = cx = cy = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'M':
                    mx, my = i, j
                elif grid[i][j] == 'C':
                    cx, cy = i, j

        dirc = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        mem = [[[[[(-1, 68) for _ in range(2)] for _ in range(n)] for _ in range(m)] for _ in range(n)] for _ in
               range(m)]

        def helper(cx, cy, mx, my, l):
            if l % 2 == 0:
                lvl1, lvl2 = mem[cx][cy][mx][my][0]
                if l <= lvl1:
                    return True
                elif l >= lvl2:
                    return False
                for dmx, dmy in dirc:
                    mX, mY, mj = mx, my, 0
                    while 0 <= mX < m and 0 <= mY < n and mj <= mouseJump:
                        if grid[mX][mY] == '#':
                            break
                        if grid[mX][mY] == 'F' or helper(cx, cy, mX, mY, l + 1):
                            mem[cx][cy][mx][my][0] = (l, lvl2)
                            return True
                        mX += dmx
                        mY += dmy
                        mj += 1
                mem[cx][cy][mx][my][0] = (lvl1, l)
                return False

            else:
                lvl1, lvl2 = mem[cx][cy][mx][my][1]
                if l <= lvl1:
                    return True
                elif l >= lvl2:
                    return False
                for dcx, dcy in dirc:
                    cX, cY, cj = cx, cy, 0
                    while 0 <= cX < m and 0 <= cY < n and cj <= catJump:
                        if grid[cX][cY] == '#':
                            break
                        if (cX == mx and cY == my) or grid[cX][cY] == 'F' or not helper(cX, cY, mx, my, l + 1):
                            mem[cx][cy][mx][my][1] = (lvl1, l)
                            return False
                        cX += dcx
                        cY += dcy
                        cj += 1
                mem[cx][cy][mx][my][1] = (l, lvl2)
                return True

        return helper(cx, cy, mx, my, 0)

# [Python/Java] 模拟

> Author: Benhao
> Date: 2021-08-08
> Upvotes: 1
> Tags: Java, Python, Python3

---

### 解题思路
比较蠢的写法，没有注意到棋盘只有8*8

### 代码

```Python3 []
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
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
```
```Java []
// https://leetcode.com/problems/check-if-move-is-legal/discuss/1389301/%400ms-oror-Java-Solution-oror-DFS-solution
class Solution {
    public boolean find(char[][] board, int rMove, int cMove, char color, int hdif, int vdif) {
            if(rMove<0 || cMove < 0 || rMove == board.length || cMove == board.length || board[rMove][cMove] == '.') return false;
            if(board[rMove][cMove] == color) return true;
            return find(board, rMove+hdif, cMove+vdif, color, hdif, vdif);
    }
    public boolean checkMove(char[][] board, int rMove, int cMove, char color) {
            int[][] dir = new int[][]{{1, 0}, {0, 1}, {1, 1}, {-1, -1}, {-1, 0}, {0, -1}, {-1, 1}, {1, -1}};
            char nc = color=='W'?'B':'W';
            for(int i=0; i<dir.length; i++) {
                int h = rMove + dir[i][0];
                int v = cMove + dir[i][1];
                if(h < 0 || v < 0 || h == 8 || v == 8 || board[h][v] != nc) {
                    continue;
                } else if(find(board, h+dir[i][0], v+dir[i][1], color, dir[i][0], dir[i][1])){
                    return true;
            }
        }
        return false;
    }
}
```
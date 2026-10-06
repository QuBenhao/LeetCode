# [Python/Java] Memoized recursion

> Author: Benhao
> Date: 2021-08-15
> Upvotes: 26
> Tags: Java, Python, Python3

---

### Approach
Return 1 whenever the position is outside the grid.
Return 0 when no moves remain.
The current answer is the sum of moving in each of the four directions, with one fewer move remaining.

[Note] Prune a state if no sequence of remaining moves can reach the boundary; its answer must be 0.

Runtime after adding pruning:
![image.png](https://pic.leetcode.cn/1628991340-yesZxk-image.png)

### Code

```python3
class Solution:
    mod = 10**9+7
    dirc = [(0,1),(0,-1),(1,0),(-1,0)]
    @lru_cache(None)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return 1 if startRow < 0 or startRow == m or startColumn < 0 or startColumn == n else (0 if not maxMove else sum(self.findPaths(m, n, maxMove - 1, startRow+dx, startColumn+dy) for dx, dy in self.dirc) % self.mod)
```
Expanded from the one-line version:
```Python3
class Solution:
    mod = 10 ** 9 + 7
    dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    @lru_cache(None)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Outside the grid
        if startRow < 0 or startRow == m or startColumn < 0 or startColumn == n:
            return 1
        # No moves remain
        if not maxMove:
            return 0
        # Sum the results of moving in all four directions
        ans = 0
        for dx, dy in self.dirc:
            ans = (ans + self.findPaths(m, n, maxMove - 1, startRow + dx, startColumn + dy)) % self.mod
        return ans
```
Prune states that cannot reach the boundary. I took a shortcut in Python; a separate memoized dfs without m and n as arguments may be faster.
```Python3 []
class Solution:
    mod = 10 ** 9 + 7
    dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    @lru_cache(None)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Outside the grid
        if startRow < 0 or startRow == m or startColumn < 0 or startColumn == n:
            return 1
        # No moves remain, or leaving the grid is impossible
        if not maxMove or (m - maxMove > startRow > maxMove - 1 and n - maxMove > startColumn > maxMove - 1):
            return 0
        # Sum the results of moving in all four directions
        ans = 0
        for dx, dy in self.dirc:
            ans = (ans + self.findPaths(m, n, maxMove - 1, startRow + dx, startColumn + dy)) % self.mod
        return ans
```
```Java []
class Solution {
    int mod = (int)1e9+7;
    int[][] dir = new int[][]{{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    int m, n;
    int[][][] dp;
    public int findPaths(int m_, int n_, int maxMove, int startRow, int startColumn) {
        m = m_;
        n = n_;
        dp = new int[maxMove][m][n];
        return dfs(maxMove, startRow, startColumn);
    }

    public int dfs(int move, int r, int c){
        if(r < 0 || r == m || c < 0 || c == n)
            return 1;
        if(move == 0 || (m - move > r && r > move - 1 && n - move > c  && c > move - 1))
            return 0;
        if(dp[--move][r][c]==0)
            for(int i=0;i<4;i++){
                int dx = dir[i][0], dy = dir[i][1];
                dp[move][r][c] = (dp[move][r][c] + dfs(move, r+dx, c+dy)) % mod;
            }
        return dp[move][r][c];
    }
}
```

### Complexity

Time complexity: $o(maxMove*m*n)$
Space complexity: $o(maxMove*m*n)$

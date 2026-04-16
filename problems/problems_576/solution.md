# [Python/Java] 记忆化递归

> Author: Benhao
> Date: 2021-08-15
> Upvotes: 26
> Tags: Java, Python, Python3

---

### 解题思路
凡是到了出界的地方，返回1；
凡是没有移动次数了，返回0；
于是当前的答案由它向四个方向移动构成(移动一次故移动次数减一)

【注意】可以剪枝，如果当前位置怎么移动也不可能到边界了，必然返回0

加入剪枝的时间如下:
![image.png](https://pic.leetcode.cn/1628991340-yesZxk-image.png)

### 代码

```python3
class Solution:
    mod = 10**9+7
    dirc = [(0,1),(0,-1),(1,0),(-1,0)]
    @lru_cache(None)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return 1 if startRow < 0 or startRow == m or startColumn < 0 or startColumn == n else (0 if not maxMove else sum(self.findPaths(m, n, maxMove - 1, startRow+dx, startColumn+dy) for dx, dy in self.dirc) % self.mod)
```
不写成一行的话:
```Python3
class Solution:
    mod = 10 ** 9 + 7
    dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    @lru_cache(None)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # 出界了
        if startRow < 0 or startRow == m or startColumn < 0 or startColumn == n:
            return 1
        # 没移动次数了
        if not maxMove:
            return 0
        # 向四个方向移动的结果的和
        ans = 0
        for dx, dy in self.dirc:
            ans = (ans + self.findPaths(m, n, maxMove - 1, startRow + dx, startColumn + dy)) % self.mod
        return ans
```
一定到达不了的剪枝(Python里我有点儿偷懒，单写一个不带m,n的dfs记忆可能更快)
```Python3 []
class Solution:
    mod = 10 ** 9 + 7
    dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    @lru_cache(None)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # 出界了
        if startRow < 0 or startRow == m or startColumn < 0 or startColumn == n:
            return 1
        # 没移动次数了或者怎么移动也不可能出界了
        if not maxMove or (m - maxMove > startRow > maxMove - 1 and n - maxMove > startColumn > maxMove - 1):
            return 0
        # 向四个方向移动的结果的和
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

### 复杂度

时间复杂度$o(maxMove*m*n)$
空间复杂度$o(maxMove*m*n)$
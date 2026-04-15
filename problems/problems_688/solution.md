# [Python/Java/JavaScript/Go] 动态规划 

> Author: Benhao
> Date: 2022-02-16
> Upvotes: 23
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
典型的第k次概率依赖于周围八个点的第k-1次概率的题目，而我们知道初始概率为1，可以从0开始递推。

### 代码
```python3
DIRS = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
class Solution:
    @lru_cache(None)
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        return 1 if not k else sum(self.knightProbability(n, k - 1, nr, nc) / 8 for dir in DIRS if 0<=(nr:=row + dir[0])<n and 0<=(nc:=column + dir[1])<n)
```
```Python3 []
DIRS = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                dp[r][c][0] = 1
        for i in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    for dir in DIRS:
                        if 0 <= (nr := r + dir[0]) < n and 0 <= (nc := c + dir[1]) < n:
                            dp[nr][nc][i] += dp[r][c][i-1] / 8
        return dp[row][column][k]
```
```Java []
class Solution {
    private static final int[][] DIRS = new int[][]{{1, 2}, {2, 1}, {-1, 2}, {2, -1}, {-2, 1}, {1, -2}, {-1, -2}, {-2, -1}};
    public double knightProbability(int n, int k, int row, int column) {
        double[][][] dp = new double[n][n][k + 1];
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                dp[i][j][0] = 1.0;
        for(int i = 1; i <= k; i++)
            for(int r = 0; r < n; r++)
                for(int c = 0; c < n; c++)
                    for(int[] dir: DIRS) {
                        int nr = r + dir[0], nc = c + dir[1];
                        if(nr >= 0 && nr < n && nc >= 0 && nc < n)
                            dp[r][c][i] += dp[nr][nc][i - 1]/8;
                    }
        return dp[row][column][k];
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number} k
 * @param {number} row
 * @param {number} column
 * @return {number}
 */
const DIRS = [[1, 2], [2, 1], [1, -2], [-2, 1], [2, -1], [-1, 2], [-1, -2], [-2, -1]]
var knightProbability = function(n, k, row, column) {
    const dp = new Array(n).fill(0).map(() => new Array(n).fill(0).map(() => new Array(k + 1).fill(0)));
    for(let i = 0; i < n; i++)
        for(let j = 0; j < n; j++)
            dp[i][j][0] = 1
    for(let i = 1; i <= k; i++)
        for(let r = 0; r < n; r++)
            for(let c = 0; c < n; c++)
                for(const dir of DIRS) {
                    const nr = r + dir[0], nc = c + dir[1]
                    if(nr >= 0 && nr < n && nc >= 0 && nc < n){
                        dp[r][c][i] += dp[nr][nc][i - 1]/8
                    }
                }
    return dp[row][column][k]
};
```
```Go []
func knightProbability(n int, k int, row int, column int) float64 {
    dp := make([][][]float64, n)
    for i := 0; i < n; i++ {
        dp[i] = make([][]float64, n)
        for j := 0; j < n; j++ {
            dp[i][j] = make([]float64, k + 1)
            dp[i][j][0] = 1
        }
    }
    for i := 1; i <= k; i++ {
        for r := 0; r < n; r++ {
            for c := 0; c < n; c++ {
                for _, dir := range [][]int{{1, 2}, {2, 1}, {-2, 1}, {1, -2}, {2, -1}, {-1, 2}, {-1, -2}, {-2, -1}} {
                    nr, nc := r + dir[0], c + dir[1]
                    if nr >= 0 && nr < n && nc >= 0 && nc < n {
                        dp[r][c][i] += dp[nr][nc][i-1]/8
                    }
                }
            }
        }
    }
    return dp[row][column][k]
}
```
滚动更新空间优化
```python3 []
DIRS = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[1] * 2 for _ in range(n)] for _ in range(n)]
        for i in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    dp[r][c][i&1] = 0
                    for dir in DIRS:
                        if 0 <= (nr := r + dir[0]) < n and 0 <= (nc := c + dir[1]) < n:
                            dp[r][c][i&1] += dp[nr][nc][(i-1)&1] / 8
        return dp[row][column][k&1]
```
```Java []
class Solution {
    private static final int[][] DIRS = new int[][]{{1, 2}, {2, 1}, {-1, 2}, {2, -1}, {-2, 1}, {1, -2}, {-1, -2}, {-2, -1}};
    public double knightProbability(int n, int k, int row, int column) {
        double[][][] dp = new double[n][n][2];
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                dp[i][j][0] = 1.0;
        for(int i = 1; i <= k; i++)
            for(int r = 0; r < n; r++)
                for(int c = 0; c < n; c++) {
                    dp[r][c][i&1] = 0;
                    for(int[] dir: DIRS) {
                        int nr = r + dir[0], nc = c + dir[1];
                        if(nr >= 0 && nr < n && nc >= 0 && nc < n)
                            dp[r][c][i&1] += dp[nr][nc][(i - 1)&1]/8;
                    }
                }
        return dp[row][column][k&1];
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number} k
 * @param {number} row
 * @param {number} column
 * @return {number}
 */
const DIRS = [[1, 2], [2, 1], [1, -2], [-2, 1], [2, -1], [-1, 2], [-1, -2], [-2, -1]]
var knightProbability = function(n, k, row, column) {
    const dp = new Array(n).fill(0).map(() => new Array(n).fill(0).map(() => new Array(2).fill(1)));
    for(let i = 1; i <= k; i++)
        for(let r = 0; r < n; r++)
            for(let c = 0; c < n; c++) {
                dp[r][c][i&1] = 0
                for(const dir of DIRS) {
                    const nr = r + dir[0], nc = c + dir[1]
                    if(nr >= 0 && nr < n && nc >= 0 && nc < n){
                        dp[r][c][i&1] += dp[nr][nc][(i - 1)&1]/8
                    }
                }
            }
    return dp[row][column][k&1]
};
```
```Go []
func knightProbability(n int, k int, row int, column int) float64 {
    dp := make([][][]float64, n)
    for i := 0; i < n; i++ {
        dp[i] = make([][]float64, n)
        for j := 0; j < n; j++ {
            dp[i][j] = make([]float64, 2)
            dp[i][j][0] = 1
        }
    }
    for i := 1; i <= k; i++ {
        for r := 0; r < n; r++ {
            for c := 0; c < n; c++ {
                dp[r][c][i&1] = 0
                for _, dir := range [][]int{{1, 2}, {2, 1}, {-2, 1}, {1, -2}, {2, -1}, {-1, 2}, {-1, -2}, {-2, -1}} {
                    nr, nc := r + dir[0], c + dir[1]
                    if nr >= 0 && nr < n && nc >= 0 && nc < n {
                        dp[r][c][i&1] += dp[nr][nc][(i-1)&1]/8
                    }
                }
            }
        }
    }
    return dp[row][column][k&1]
}
```
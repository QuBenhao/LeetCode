# [Python/Java/Go] 动态规划

> Author: Benhao
> Date: 2022-02-21
> Upvotes: 1
> Tags: Go, Java, Python, Python3

---

### 解题思路
到右下角的点的路径数由它的左边那个点和上边那个点构成

注:
```
Python: cache实现简单代码
Java: static一次获取全部结果
Go: 滚动更新写法
```

### 代码

```Python3 []
class Solution:
    @lru_cache(None)
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1) if m - 1 and n - 1 else 1
```
```Java []
class Solution {
    private static final int[][] dp = new int[100][100];
    static {
        for(int i = 0; i < 100; i++)
            for(int j = 0; j < 100; j++)
                dp[i][j] = i == 0 || j == 0 ? 1 : dp[i - 1][j] + dp[i][j - 1];
    }
    public int uniquePaths(int m, int n) {
        return dp[m - 1][n - 1];
    }
}
```
```Go []
func uniquePaths(m int, n int) int {
    dp := make([][]int, 2)
    dp[0] = make([]int, n)
    dp[1] = make([]int, n)
    for i := 0; i < n; i++ {
        dp[0][i]++
    }
    for i := 1; i < m; i++ {
        dp[i&1][0] = 1
        for j := 1; j < n; j++ {
            dp[i&1][j] = dp[(i-1)&1][j] + dp[i&1][j - 1]
        }
    }
    return dp[(m - 1)&1][n - 1]
}
```
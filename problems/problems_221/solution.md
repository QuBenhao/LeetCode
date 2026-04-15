# [Python/Go] 动态规划(滚动更新)

> Author: Benhao
> Date: 2022-02-22
> Upvotes: 1
> Tags: Go, Python, Python3

---

### 解题思路
当前能组成的最大正方形变成由，左上角、上方、左边的点能组成的最大正方形的最小值在加上当前自己的1构成。
加入左上角只能构成一个边长为1的正方形，那么当前最多能构成边长为2的正方形。
同理，上方和左边都会对当前点造成影响。

### 代码

```Python3 []
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans, m, n = 0, len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(2)]
        for i in range(m):
            for j in range(n):
                b = matrix[i][j] == '1'
                dp[i&1][j] = int(b)
                if i and j and b:
                    dp[i&1][j] = 1 + min(dp[(i - 1)&1][j - 1], dp[(i - 1)&1][j], dp[i&1][j - 1])
                ans = max(ans, dp[i&1][j])
        return ans ** 2
```
```Go []
func maximalSquare(matrix [][]byte) (ans int) {
    m, n := len(matrix), len(matrix[0])
    dp := make([][]int, 2)
    dp[0], dp[1] = make([]int, n), make([]int, n)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if matrix[i][j] == '1' {
                dp[i & 1][j] = 1
                if i > 0 && j > 0{
                    dp[i & 1][j] += min(dp[(i - 1) & 1][j], dp[(i - 1) & 1][j - 1], dp[i & 1][j - 1])
                }
                ans = max(ans, dp[i & 1][j])
            } else {
                dp[i & 1][j] = 0
            }
        }
    }
    ans *= ans
    return
}

func min(vals ...int) int {
    ans := vals[0]
    for _, v := range vals {
        if v < ans {
            ans = v
        }
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```
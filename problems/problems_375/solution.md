# [Python/Java/JavaScript/Go] 记忆化递归 or 动态规划

> slug: python-ji-yi-hua-di-gui-by-himymben-8o8z
> date: 2021-11-11
> tags: Go, Java, JavaScript, Python, Python3
> question: Guess Number Higher or Lower II (guess-number-higher-or-lower-ii)
> url: https://leetcode.cn/problems/guess-number-higher-or-lower-ii/solutions/aNqqS0/python-ji-yi-hua-di-gui-by-himymben-8o8z/

---
```python3
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # 如果猜数字大小k，而答案不是k的话，问题变为求解 (1, k-1) 和 (k+1, n) 的子问题需要的代价的最大值
        @lru_cache(None)
        def dfs(x, y):
            return min(max(dfs(x, k-1), dfs(k+1, y)) + k for k in range(x, y + 1)) if y > x else 0
        return dfs(1, n)
```
```Python3 []
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # 如果猜数字大小k，而答案不是k的话，问题变为求解 (1, k-1) 和 (k+1, n) 的子问题需要的代价的最大值
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n-1,0,-1):
            for j in range(i+1, n+1):
                dp[i][j] = min(max(dp[i][k-1], dp[k+1][j]) + k for k in range(i, j))
        return dp[1][-1]
```
```Java []
class Solution {
    public int getMoneyAmount(int n) {
        int[][] dp = new int[n+1][n+1];
        for(int i=n-1;i>0;i--)
            for(int j=i+1;j<=n;j++){
                int min = Integer.MAX_VALUE;
                for(int k=i;k<j;k++)
                    min = Math.min(min, Math.max(dp[i][k-1], dp[k+1][j]) + k);
                dp[i][j] = min;
            }
        return dp[1][n];
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var getMoneyAmount = function(n) {
    const dp = new Array(n + 1).fill(0).map(() => new Array(n + 1).fill(0));
    for (let i = n - 1; i >= 1; i--) {
        for (let j = i + 1; j <= n; j++) {
            let m = Number.MAX_VALUE;
            for (let k = i; k < j; k++)
                m = Math.min(m, Math.max(dp[i][k - 1], dp[k + 1][j]) + k);
            dp[i][j] = m;
        }
    }
    return dp[1][n];
};
```
```Go []
func getMoneyAmount(n int) int {
    dp := make([][]int, n + 1)
    for i:=0;i<=n;i++ {
        dp[i] = make([]int, n + 1)
    }
    for i:=n-1;i>0;i--{
        for j:=i+1;j<=n;j++{
            m := math.MaxInt32
            for k:=i;k<j;k++{
                if dp[i][k-1] > dp[k+1][j]{
                    if v:=dp[i][k-1]+k; m > v {
                        m = v
                    }
                } else{
                    if v:=dp[k+1][j]+k; m > v {
                        m = v
                    }                
                }
            }
            dp[i][j] = m
        }
    }
    return dp[1][n]
}
```
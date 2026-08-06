# [Python/Java/JavaScript/Go] 记忆化递归 or 动态规划

> slug: python-ji-yi-hua-di-gui-by-himymben-bujz
> date: 2021-11-10
> tags: Go, Java, JavaScript, Python, Python3
> question: K Inverse Pairs Array (k-inverse-pairs-array)
> url: https://leetcode.cn/problems/k-inverse-pairs-array/solutions/mlDAEA/python-ji-yi-hua-di-gui-by-himymben-bujz/

---
### 解题思路
这题和[1866](https://leetcode.cn/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/solution/python-kao-lu-mei-ci-fang-zhi-de-du-shi-mskpw/)的思路可以说如出一辙了

假设现在有`n`个位置给`最大的数字`选，那么它放在`第一个`，就会产生`n-1`个逆序对，剩下的情况变为`n-1个数字`需要产生`k-(n-1)`个逆序对.
假设现在有`n`个位置给`最大的数字`选，那么它放在`第二个`，就会产生`n-2`个逆序对，剩下的情况变为`n-1个数字`需要产生`k-(n-2)`个逆序对.
...（以此类推）
假设现在有`n`个位置给`最大的数字`选，那么它放在`倒数第一个`，就会产生`0`个逆序对，剩下的情况变为`n-1个数字`需要产生`k`个逆序对.

```python
# 模拟最大的填入的位置， 进行递归
# dp[n][k] = dp[n-1][k] + dp[n-1][k-1] + dp[n-1][k-2] + dp[n-1][k-3] + ... + dp[n-1][k-(n-1)]
# 当前的连续和其实大部分都由上一个连续和求过了
# dp[n][k-1] =            dp[n-1][k-1] + dp[n-1][k-2] + dp[n-1][k-3] + ... + dp[n-1][k-(n-1)] + dp[n-1][k-1-(n-1)]
# 错位相减简化式子
# dp[n][k] - dp[n][k-1] = dp[n-1][k] - dp[n-1][k-n] if k >= n else dp[n-1][k]
```

### 代码

```python3
MOD = int(1e9) + 7
class Solution:
    @staticmethod
    @lru_cache(None)
    def kInversePairs(n: int, k: int) -> int:
        return (Solution.kInversePairs(n, k-1) + Solution.kInversePairs(n-1, k)- (Solution.kInversePairs(n-1, k-n) if k >= n else 0)) % MOD if n > 1 and k else int(n > k)
```

```Python3 []
MOD = int(1e9) + 7
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # dp[n][k] - dp[n][k-1] = dp[n-1][k] - dp[n-1][k-n] if k >= n else dp[n-1][k]
        dp = [1] + [0] * k
        for i in range(2, n + 1):
            next_dp = [1] + [0] * k
            for j in range(1, k + 1):
                next_dp[j] = (next_dp[j-1] + dp[j] - (dp[j-i] if j >= i else 0)) % MOD
            dp = next_dp
        return dp[-1] 
```
```Java []
class Solution {
    private static final int MOD = 1000000007;
    public int kInversePairs(int n, int k) {
        // dp[n][k] - dp[n][k-1] = dp[n-1][k] - dp[n-1][k-n] if k >= n else dp[n-1][k]
        int[] dp = new int[k + 1];
        Arrays.fill(dp, 0);
        dp[0] = 1;
        for(int i=2;i<=n;i++){
            int[] next_dp = new int[k + 1];
            Arrays.fill(next_dp, 0);
            next_dp[0] = 1;
            for(int j=1;j<=k;j++){
                next_dp[j] = (next_dp[j-1] + dp[j]) % MOD;
                if(j >= i){
                    next_dp[j] = (next_dp[j] - dp[j-i] + MOD) % MOD;
                }
            }
            dp = next_dp;
        }
        return dp[k];
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
const MOD = 1000000007;
var kInversePairs = function(n, k) {
    // dp[n][k] - dp[n][k-1] = dp[n-1][k] - dp[n-1][k-n] if k >= n else dp[n-1][k]
    let dp = new Array(k + 1);
    dp.fill(0);
    dp[0] = 1;
    for(let i=2;i<=n;i++){
        const next_dp = new Array(k + 1);
        next_dp.fill(0);
        next_dp[0] = 1;
        for(let j=1;j<=k;j++){
            next_dp[j] = (next_dp[j-1] + dp[j]) % MOD;
            if(j >= i){
                next_dp[j] = (next_dp[j] - dp[j-i] + MOD) % MOD;
            }
        }
        dp = next_dp;
    }
    return dp[k];
};
```
```Go []
func kInversePairs(n int, k int) int {
    // dp[n][k] - dp[n][k-1] = dp[n-1][k] - dp[n-1][k-n] if k >= n else dp[n-1][k]
    MOD := 1000000007
    dp := make([]int, k + 1)
    dp[0] = 1
    for i := 2; i <= n; i++ {
        next_dp := make([]int, k + 1)
        next_dp[0] = 1
        for j := 1; j <= k; j++{
            next_dp[j] = (dp[j] + next_dp[j-1]) % MOD
            if j >= i {
                next_dp[j] = (next_dp[j] - dp[j-i] + MOD) % MOD
            }
        }
        dp = next_dp
    }
    return dp[k]
}
```
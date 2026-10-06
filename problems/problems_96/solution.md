# [Python/Go] Dynamic programming

> slug: pythongo-dong-tai-gui-hua-by-himymben-tngf
> date: 2022-02-17
> tags: Go, Python, Python3
> question: Unique Binary Search Trees (unique-binary-search-trees)
> url: https://leetcode.cn/problems/unique-binary-search-trees/solutions/SFRDmC/pythongo-dong-tai-gui-hua-by-himymben-tngf/

---
### Approach
Choose a value i from 1 through n as the root of the binary search tree.
The left subtree is formed recursively from the i-1 values smaller than i, and the right subtree from the n-i values greater than i.

### Code

```Python3 []
class Solution:
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        return sum(self.numTrees(i - 1) * self.numTrees(n - i) for i in range(1, n + 1)) if n > 1 else 1
```
```Go []
func numTrees(n int) int {
    dp := make([]int, n + 1)
    dp[0], dp[1] = 1, 1
    for i := 2; i <= n; i++ {
        for j := 1; j <= i; j++ {
            dp[i] += dp[j - 1] * dp[i - j]
        }
    }
    return dp[n]
}
```

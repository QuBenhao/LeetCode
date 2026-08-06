# [Python/Go] 动态规划

> slug: pythongo-dong-tai-gui-hua-by-himymben-tngf
> date: 2022-02-17
> tags: Go, Python, Python3
> question: Unique Binary Search Trees (unique-binary-search-trees)
> url: https://leetcode.cn/problems/unique-binary-search-trees/solutions/SFRDmC/pythongo-dong-tai-gui-hua-by-himymben-tngf/

---
### 解题思路
找1到n之间的某一个点i作为二叉搜索树的根节点，
那么左子树由小于i的i-1个数构成（递归），右子树由大于i的n-i个数构成（递归）

### 代码

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
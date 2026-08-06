# [Python/Go] 记忆化递归 || 状态压缩动态规划

> slug: python-ji-yi-hua-di-gui-by-himymben-pnq1
> date: 2022-02-13
> tags: Go, Python, Python3
> question: Maximum AND Sum of Array (maximum-and-sum-of-array)
> url: https://leetcode.cn/problems/maximum-and-sum-of-array/solutions/4LyDDU/python-ji-yi-hua-di-gui-by-himymben-pnq1/

---
### 解题思路

枚举盒子的状态即可，和状态压缩一样

### 代码

```Python3 []
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        @lru_cache(None)
        def dfs(idx, state):
            if idx == len(nums):
                return 0
            st, res = list(state), 0
            for i, s in enumerate(state):
                if s < 2:
                    st[i] += 1
                    res = max(res, dfs(idx + 1, tuple(st)) + ((i + 1) & nums[idx]))
                    st[i] -= 1
            return res
        
        return dfs(0, tuple([0] * numSlots))
```
```Go []
func maximumANDSum(nums []int, numSlots int) (ans int) {
    dp := make([]int, 1 << (numSlots * 2))
    for i, f := range dp {
        // 已经填了几个数
        idx := bitCounts(i, numSlots * 2)
        if idx < len(nums) {
            for j := 0; j < numSlots * 2; j++ {
                if i >> j & 1 == 0 {
                    other := i | 1 << j
                    dp[other] = max(dp[other], f + (j/2 + 1) & nums[idx])
                    ans = max(ans, dp[other])
                }
            }
        }
    }
    return
}

func bitCounts(num int, m int) (ans int) {
    for j := 0; j < m; j++ {
        if num & 1 == 1 {
            ans++
        }
        num >>= 1
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```
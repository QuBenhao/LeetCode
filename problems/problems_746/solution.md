# [Python/Go] 动态规划 

> slug: pythongo-dong-tai-gui-hua-by-himymben-xcpe
> date: 2022-02-08
> tags: Go, Python, Python3
> question: Min Cost Climbing Stairs (min-cost-climbing-stairs)
> url: https://leetcode.cn/problems/min-cost-climbing-stairs/solutions/BBMU0c/pythongo-dong-tai-gui-hua-by-himymben-xcpe/

---
### 解题思路
维护走到当前阶梯和上一个阶梯的最小值

### 代码

```Python3 []
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx):
            return 0 if idx >= len(cost) else min(dfs(idx + 1), dfs(idx + 2)) + cost[idx]
        return min(dfs(0), dfs(1))
```
```Go []
func minCostClimbingStairs(cost []int) int {
    a, b := cost[0], cost[1]
    for _, c := range cost[2:] {
        a, b = b, min(a, b) + c
    }
    return min(a, b)
}

func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}
```
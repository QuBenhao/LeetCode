# [Python] DP or 记忆化搜索

> Author: Benhao
> Date: 2024-04-22
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---

### 代码

```Python3 []
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i < num:
                    break
                dp[i] += dp[i - num]
        return dp[target]
```
```Python3 []
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort(reverse=True)
        @lru_cache(None)
        def dfs(v):
            if not v:
                return 1
            return sum(dfs(v - num) for num in nums if num <= v)
        
        return dfs(target)
```
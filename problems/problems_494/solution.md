# [Python] From memoized search to dynamic programming

> Author: Benhao
> Date: 2021-06-06
> Upvotes: 10
> Tags: Python, Python3

---

### Approach
**Search** can be sped up slightly with prefix-sum pruning, somewhat like A*.

**Dynamic programming** begins with a mathematical transformation:
```python3
        # target is the sum of values assigned + minus the sum of values assigned -
        # If the positive-side sum is a, the negative-side sum is sum - a, and a-(sum-a) = target
        # Thus, a = (target+sum)//2
        # Count combinations whose sum is (target+sum)//2
```
The problem becomes counting combinations in nums with sum (target+sum(nums))//2, a knapsack problem where each value is taken or skipped.

### Code
Memoized search
```python3
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(idx, t):
            if idx == n:
                if t == target:
                    return 1
                return 0
            # The target is unreachable even if all remaining values are positive or all are negative
            if abs(target - t) > presum[-1] - presum[idx]:
                return 0
            return dfs(idx+1, t+nums[idx]) + dfs(idx+1, t-nums[idx])
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(n):
            presum[i+1] = presum[i] + nums[i]
        return dfs(0, 0)
```
Dynamic programming
```python3
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # target is the sum of values assigned + minus the sum of values assigned -
        # If the positive-side sum is a, the negative-side sum is s - a, and a-(s-a) = target
        # Thus, a = (target+s)//2
        # Count combinations whose sum is (target+s)//2
        t = target + sum(nums)
        if t % 2 != 0 or t < 0 or t - target * 2 < 0:
            return 0
        t //= 2
        dp = [0] * (t+1)
        dp[0] = 1
        for num in nums:
            # Update backward: each previous way to reach i-num yields another way to reach i by taking num
            for i in range(t,num-1,-1):
                dp[i] += dp[i-num]
        return dp[t]
```
Dictionary-based dynamic programming (precompute the contribution of zeros)
```python3
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # target is the sum of values assigned + minus the sum of values assigned -
        # If the positive-side sum is a, the negative-side sum is s - a, and a-(s-a) = target
        # Thus, a = (target+s)//2
        # Count combinations whose sum is (target+s)//2
        t = target + sum(nums)
        if t % 2 != 0 or t < 0 or t - target * 2 < 0:
            return 0
        t //= 2
        dp = Counter()
        dp[0] = 2 ** nums.count(0)
        for num in nums:
            if not num:
                continue
            for key in sorted(dp.keys(), reverse=True):
                if key <= t - num:
                    dp[num+key] += dp[key]
        return dp[t]
```

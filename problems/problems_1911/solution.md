# [Python] Dynamic programming with rolling updates

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Each position has four DP values for the maximum total so far: include or exclude the current number, ending in either subtraction (the next number is added) or addition (the next number is subtracted).
The final result must end in addition, either including or excluding the current number, so it is in dp1 or dp3.

Time complexity: o(n); space complexity: o(1)

### Code

```python3
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][0]: include i, end with -; dp[i][1]: include i, end with +; dp[i][2]: exclude i, end with -; dp[i][3]: exclude i, end with +
        dp0 = dp2 = dp3 = 0
        dp1 = nums[0]
        for i in range(1, n):
            dp0, dp1, dp2, dp3 = max(dp1 - nums[i], dp3 - nums[i]),\
                                 max(dp0 + nums[i], dp2 + nums[i]),\
                                 max(dp0, dp2),\
                                 max(dp1, dp3)
        return max(dp1, dp3)
```

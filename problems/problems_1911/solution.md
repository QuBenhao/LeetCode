# [Python] 动态规划（滚动更新）

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
每个位置有四种dp值，从第一个数累加到现在的最大值: 包不包含自己作为-结尾(下一个数就可以+)，包不包含自己作为+结尾(下一个数必须-)
最终结果必然是取+的，包不包含自己的在dp1或dp3里的一个

时间复杂度o(n),空间复杂度o(1)

### 代码

```python3
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][0] 作为-结尾,dp[i][1]作为+结尾,dp[i][2]不包含i结尾为-，dp[i][3]不包含i结尾为+
        dp0 = dp2 = dp3 = 0
        dp1 = nums[0]
        for i in range(1, n):
            dp0, dp1, dp2, dp3 = max(dp1 - nums[i], dp3 - nums[i]),\
                                 max(dp0 + nums[i], dp2 + nums[i]),\
                                 max(dp0, dp2),\
                                 max(dp1, dp3)
        return max(dp1, dp3)
```
# [Python] 动态规划

> slug: -by-himymben-qvhp
> date: 2022-03-27
> tags: Python, Python3
> question: Minimum Deletions to Make Array Beautiful (minimum-deletions-to-make-array-beautiful)
> url: https://leetcode.cn/problems/minimum-deletions-to-make-array-beautiful/solutions/tYtGSv/-by-himymben-qvhp/

---
### 解题思路
dp[i]表示以i为开头，删成满足题目条件的最小代价。根据nums[i]和nums[i+1]是否相等从后往前递推即可。

假如nums[i]和nums[i+1]相等，那么必然不能以nums[i]开头，我们需要删掉nums[i]，也即dp[i] = dp[i+1] + 1，
而如果不相等，可以不做处理，和以nums[i+2]开头删的次数一样，即dp[i] = dp[i+2]

在初始化时，dp[len(nums)]本身是空数组，不需要删就满足条件，所以dp[-1] = 0,
而dp[len(nums)-1]是奇数长度的，必须删掉自己，所以dp[-2] = 1

### 代码

```python3
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[-2] = 1
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = dp[i + 1] + 1 if nums[i] == nums[i + 1] else dp[i + 2]
        return dp[0]
```
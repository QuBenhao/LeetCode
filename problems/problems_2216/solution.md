# [Python] Dynamic programming

> slug: -by-himymben-qvhp
> date: 2022-03-27
> tags: Python, Python3
> question: Minimum Deletions to Make Array Beautiful (minimum-deletions-to-make-array-beautiful)
> url: https://leetcode.cn/problems/minimum-deletions-to-make-array-beautiful/solutions/tYtGSv/-by-himymben-qvhp/

---
### Approach
dp[i] is the minimum number of deletions needed to make the suffix starting at i satisfy the conditions. Work backward according to whether nums[i] and nums[i+1] are equal.

If nums[i] and nums[i+1] are equal, the result cannot start with nums[i], so delete it: dp[i] = dp[i+1] + 1.
If they differ, keep both; the deletion count is the same as for the suffix starting at nums[i+2], so dp[i] = dp[i+2].

For initialization, dp[len(nums)] represents an empty array, which already satisfies the conditions, so dp[-1] = 0.
dp[len(nums)-1] has odd length and must delete its only element, so dp[-2] = 1.

### Code

```python3
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[-2] = 1
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = dp[i + 1] + 1 if nums[i] == nums[i + 1] else dp[i + 2]
        return dp[0]
```

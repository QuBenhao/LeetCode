# [Python] 动态规划

> slug: python-dong-tai-gui-hua-by-himymben-skeb
> date: 2022-05-03
> tags: Python, Python3
> question: Maximum Alternating Subarray Sum (maximum-alternating-subarray-sum)
> url: https://leetcode.cn/problems/maximum-alternating-subarray-sum/solutions/Vy3Bx0/python-dong-tai-gui-hua-by-himymben-skeb/

---
### 解题思路
遍历统计以i结尾的最大结果，这个最大结果由上一次加结尾的最大值或减结尾的最大值构成。

### 代码

```python3
class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        ans, dp0, dp1 = nums[0], nums[0], -inf
        for num in nums[1:]:
            dp0, dp1 = max(num, dp1 + num), dp0 - num
            ans = max(ans, dp0, dp1)
        return ans

```
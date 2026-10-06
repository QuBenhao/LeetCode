# [Python] Dynamic programming

> slug: python-dong-tai-gui-hua-by-qubenhao-fpa4
> date: 2021-07-16
> tags: Python, Python3
> question: 连续天数的最高销售额 (lian-xu-zi-shu-zu-de-zui-da-he-lcof)
> url: https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/solutions/gv3CSV/python-dong-tai-gui-hua-by-qubenhao-fpa4/

---
### Approach
Use cur to track the maximum subarray sum ending at each num: either the previous maximum plus the current value, or the current value alone.
Keep the largest cur.

### Code

```python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, cur = -inf, 0
        for num in nums:
            cur = max(cur + num, num)
            ans = max(ans, cur)
        return ans
```

# [Python] 动态规划

> slug: python-dong-tai-gui-hua-by-qubenhao-fpa4
> date: 2021-07-16
> tags: Python, Python3
> question: 连续天数的最高销售额 (lian-xu-zi-shu-zu-de-zui-da-he-lcof)
> url: https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/solutions/gv3CSV/python-dong-tai-gui-hua-by-qubenhao-fpa4/

---
### 解题思路
用cur统计到每一个num时的最大值(要么是前一个最大值加上当前值，要么是当前值)
记录最大的cur即可。

### 代码

```python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, cur = -inf, 0
        for num in nums:
            cur = max(cur + num, num)
            ans = max(ans, cur)
        return ans
```
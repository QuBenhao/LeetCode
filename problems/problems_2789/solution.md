# [Python] 贪心

> slug: python-tan-xin-by-himymben-ag4d
> date: 2024-03-14
> tags: C, Go, Java, Python3, TypeScript
> question: Largest Element in an Array after Merge Operations (largest-element-in-an-array-after-merge-operations)
> url: https://leetcode.cn/problems/largest-element-in-an-array-after-merge-operations/solutions/atIADI/python-tan-xin-by-himymben-ag4d/

---

> Problem: [2789. 合并后数组中的最大元素](https://leetcode.cn/problems/largest-element-in-an-array-after-merge-operations/description/)

[TOC]

# 思路

> 从后往前能吞就吞，不能吞则从现在的大小重新出发，继续往前看，找最大的答案

# 解题方法

> 贪心模拟

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$


# Code
```Python3 []
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ans = cur = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if cur >= nums[i]:
                cur += nums[i]
            else:
                cur = nums[i]
            ans = max(ans, cur)
        return ans
```
  

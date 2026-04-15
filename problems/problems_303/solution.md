# [Python] 前缀和

> Author: Benhao
> Date: 2024-03-18
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [303. 区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/description/)

[TOC]

# 思路

> 前缀和

# 解题方法

> 可以用来在数组中快速求任意区间的和

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = [0] + list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right + 1] - self.presum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```
  

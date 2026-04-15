# [Python] 维护最小前缀和

> Author: Benhao
> Date: 2024-03-03
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/description/)

[TOC]

# 思路

> 求最大区间和相当于求前面最小的前缀和以及当前前缀和的差的最大值

# 解题方法

> 遍历维护一个最小前缀和，最终答案由某位置的最大结果构成

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, pre, m = -inf, 0, 0
        for num in nums:
            pre += num
            ans = max(ans, pre - m)
            m = min(pre, m)
        return ans
```
另外写一遍经典的 
divide and conquer
```Python3 []
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def div_and_con(left, right):
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            ld, rd = div_and_con(left, mid), div_and_con(mid + 1, right)
            lmax, ls = -inf, 0
            for i in range(mid, left - 1, -1):
                ls += nums[i]
                lmax = max(lmax, ls)
            rmax, rs = -inf, 0
            for i in range(mid + 1, right + 1):
                rs += nums[i]
                rmax = max(rmax, rs)
            return max(ld, rd, lmax + rmax)
        
        return div_and_con(0, len(nums) - 1)
```

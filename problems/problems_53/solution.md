# [Python] Maintain the minimum prefix sum

> Author: Benhao
> Date: 2024-03-03
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/description/)

[TOC]

# Intuition

> Finding the maximum subarray sum is equivalent to maximizing the difference between the current prefix sum and the smallest preceding prefix sum.

# Approach

> Maintain the minimum prefix sum while traversing; the final answer is the largest result at any position.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
Here is the classic approach as well. 
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

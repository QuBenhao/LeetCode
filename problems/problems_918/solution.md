# [Python] 最大最小子数组和

> slug: python-zui-da-zui-xiao-zi-shu-zu-he-by-h-emfb
> date: 2024-03-11
> tags: C, Go, Java, Python3, TypeScript
> question: Maximum Sum Circular Subarray (maximum-sum-circular-subarray)
> url: https://leetcode.cn/problems/maximum-sum-circular-subarray/solutions/LfSDvE/python-zui-da-zui-xiao-zi-shu-zu-he-by-h-emfb/

---

> Problem: [918. 环形子数组的最大和](https://leetcode.cn/problems/maximum-sum-circular-subarray/description/)

[TOC]

# 思路

> 环形最大子数组和包括普通子数组和，以及前面一部分子数组+后面一部分子数组，求这个的最大值相当于求减去它的最小值，即中间的最小子数组和

# 解题方法

> 如果最大子数组和为负数，说明数组全是负数，那么最小子数组一定会选全部，差为0，排除掉这种答案即可

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$

# Code
```Python3 []
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s, max_pre, max_ans, min_pre, min_ans = 0, -inf, -inf, 0, 0
        for num in nums:
            # 包含num的最大前缀和
            max_pre = max(num, max_pre + num)
            # 最大子数组和
            max_ans = max(max_ans, max_pre)
            # 包含num的最小前缀和
            min_pre = min(num, min_pre + num)
            # 最小子数组和
            min_ans = min(min_ans, min_pre)
            s += num
        # 环形最大子数组和 = 总和 - 最小子数组和
        return max(max_ans, s - min_ans) if max_ans > 0 else max_ans
```
  

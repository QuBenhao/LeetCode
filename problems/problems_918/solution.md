# [Python] Maximum and minimum subarray sums

> slug: python-zui-da-zui-xiao-zi-shu-zu-he-by-h-emfb
> date: 2024-03-11
> tags: C, Go, Java, Python3, TypeScript
> question: Maximum Sum Circular Subarray (maximum-sum-circular-subarray)
> url: https://leetcode.cn/problems/maximum-sum-circular-subarray/solutions/LfSDvE/python-zui-da-zui-xiao-zi-shu-zu-he-by-h-emfb/

---

> Problem: [918. 环形子数组的最大和](https://leetcode.cn/problems/maximum-sum-circular-subarray/description/)

[TOC]

# Intuition

> The maximum circular subarray sum may come from a regular subarray or from a prefix plus a suffix. Maximizing the latter is equivalent to subtracting the smallest middle subarray sum from the total

# Approach

> If the maximum subarray sum is negative, every value is negative. The minimum subarray would then include the entire array, leaving a difference of 0; exclude this answer

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$

# Code
```Python3 []
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s, max_pre, max_ans, min_pre, min_ans = 0, -inf, -inf, 0, 0
        for num in nums:
            # Maximum prefix sum containing num
            max_pre = max(num, max_pre + num)
            # Maximum subarray sum
            max_ans = max(max_ans, max_pre)
            # Minimum prefix sum containing num
            min_pre = min(num, min_pre + num)
            # Minimum subarray sum
            min_ans = min(min_ans, min_pre)
            s += num
        # Maximum circular subarray sum = total sum - minimum subarray sum
        return max(max_ans, s - min_ans) if max_ans > 0 else max_ans
```
  

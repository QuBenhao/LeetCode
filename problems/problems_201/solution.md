# [Python] Compare the common prefix bits

> Author: Benhao
> Date: 2024-03-21
> Upvotes: 0
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [201. 数字范围按位与](https://leetcode.cn/problems/bitwise-and-of-numbers-range/description/)

[TOC]

# Intuition

> Suppose the kth bit from the right is 0 in left and 1 in right. We no longer need to inspect that bit or any lower bits: the interval must contain a number whose kth bit is 1 and whose lower k-1 bits are all 0.

> For example, consider the binary numbers [1, 0, 1, 1] and [1, 1, 1, 1]. The third bit from the right in left is 0, so [left,right] must include [1,1,0,0], and [1,1,0,0] & [1,0,1,1] = [1, 0, 0, 0]. Therefore, the remaining bits do not need to be processed.

# Approach

> Find the 1 bits in the common prefix

# Complexity

Time complexity:
> $O(1)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        for i in range(31, -1, -1):
            cur = 1 << i
            l, r = left & cur, right & cur
            if r > 0 and l == 0:
                return ans
            if r > 0 and l > 0:
                ans |= 1 << i
        return ans
```
  

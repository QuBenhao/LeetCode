# [Python] 比较前缀1

> Author: Benhao
> Date: 2024-03-21
> Upvotes: 0
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [201. 数字范围按位与](https://leetcode.cn/problems/bitwise-and-of-numbers-range/description/)

[TOC]

# 思路

> 假设我们在二进制最低k位时，left值为0，right值为1，那么从最低k位到最低位我们都不用再看了，因为这个区间必然包括最低k位为1，剩下最低k-1位到最低位为0这个数。

> 比如: 两个二进制数[1, 0, 1, 1], [1, 1, 1, 1]，我们注意到left最低3位为0,那么[left,right]区间必然包括[1,1,0,0]这个数，而[1,1,0,0] & [1,0,1,1] = [1, 0, 0, 0]。所以剩下的位是不需要再计算了的

# 解题方法

> 找前缀1

# 复杂度

时间复杂度:
> $O(1)$

空间复杂度:
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
  

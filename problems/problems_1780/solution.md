# Base 3

> Author: Benhao
> Date: 2022-12-08
> Upvotes: 22
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1780. 判断一个数字是否可以表示成三的幂的和](https://leetcode.cn/problems/check-if-number-is-a-sum-of-powers-of-three/description/)

[TOC]

# Intuition
> A sum of distinct powers of 3 has only 0 and 1 digits in base 3.

# Approach
> Convert to base 3 and ensure no digit is 2.

# Complexity
- Time complexity:
> $O(log_{3}n)$

- Space complexity:
> $O(1)$

# Code
```Python3 []

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2:
                return False
            n //= 3
        return True
```
```Go []
func checkPowersOfThree(n int) bool {
    for ; n > 0; n /= 3 {
        if n % 3 == 2 {
            return false
        }
    }
    return true
}
```

# 三进制

> Author: Benhao
> Date: 2022-12-08
> Upvotes: 22
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1780. 判断一个数字是否可以表示成三的幂的和](https://leetcode.cn/problems/check-if-number-is-a-sum-of-powers-of-three/description/)

[TOC]

# 思路
> 一个数可以表示为不同的3的幂次的和，那么它的三进制每一位只能是1或0

# 解题方法
> 按三进制转换，确保三进制任意位中没有2

# 复杂度
- 时间复杂度: 
> $O(log_{3}n)$

- 空间复杂度: 
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

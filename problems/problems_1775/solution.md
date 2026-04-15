# 贪心

> Author: Benhao
> Date: 2022-12-07
> Upvotes: 10
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1775. 通过最少操作次数使数组的和相等](https://leetcode.cn/problems/equal-sum-arrays-with-minimum-number-of-operations/description/)

[TOC]

# 思路
> 数字和较小的数组尽可能将数变成6，数字和较大的数组尽可能将数变成1，这样的操作数最少。那么我们统计和小的数组的数，以及和大的数组的对称数，贪心计算结果即可

# 解题方法
> 和较小的数组里的1与和较大的数组里的6是对称的，所以在统计数字频率时，将两者映射

# Code
```Python3 []
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2:
            return self.minOperations(nums2, nums1)
        elif s1 == s2:
            return 0
        ans, diff, cnts, i = 0, s2 - s1, Counter(nums1 + [7 - num for num in nums2]), 1
        while diff and i <= 5:
            for _ in range(cnts[i]):
                if not diff:
                    break
                if diff >= 6 - i:
                    diff -= 6 - i
                else:
                    diff = 0 
                ans += 1 
            i += 1
        return -1 if diff > 0 else ans
```
```Go []
func minOperations(nums1 []int, nums2 []int) (ans int) {
    s1, s2 := sum(nums1), sum(nums2)
    if s1 > s2 {
        return minOperations(nums2, nums1)
    } else if s1 == s2 {
        return
    }
    diff, cnts := s2 - s1, map[int]int{}
    for _, num := range nums1 {
        cnts[num]++
    }
    for _, num := range nums2 {
        cnts[7 - num]++
    }
    for i := 1; diff > 0 && i <= 5; i++ {
        for j := 0; j < cnts[i]; j++ {
            if diff == 0 {
                break
            }
            if diff > 6 - i {
                diff -= 6 - i
            } else {
                diff = 0
            }
            ans++
        }
    }
    if diff > 0 {
        return -1
    }
    return
}

func sum(nums []int) (ans int) {
    for _, num := range nums {
        ans += num
    }
    return
}
```

# [Python/Go/C] 前缀后缀

> Author: Benhao
> Date: 2024-02-26
> Upvotes: 3
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [238. 除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/description/)

[TOC]

# 思路

> 答案每个位置的数目为该位置的数组前缀积*数组后缀积

# 解题方法

> 遍历维护前缀积，再遍历求后缀积从而得到答案

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suf
            suf *= nums[i] 
        return res
```
```Go []
func productExceptSelf(nums []int) []int {
    n := len(nums)
    ans := make([]int, n)
    ans[0] = 1
    for i := 1; i < n; i++ {
        ans[i] = ans[i - 1] * nums[i - 1]
    }
    suf := 1
    for i := n - 1; i >= 0; i-- {
        ans[i] *= suf
        suf *= nums[i]
    }
    return ans
}
```
```C []
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int *ans = malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;
    ans[0] = 1;
    for (int i = 1; i < numsSize; i++) {
        ans[i] = ans[i - 1] * nums[i - 1];
    }
    int suf = 1;
    for (int i = numsSize - 1; i >= 0; i--) {
        ans[i] *= suf;
        suf *= nums[i];
    }
    return ans;
}
```
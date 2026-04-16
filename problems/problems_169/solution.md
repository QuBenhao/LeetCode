# [Python/Go/C] 多数投票

> Author: Benhao
> Date: 2024-02-23
> Upvotes: 28
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [169. 多数元素](https://leetcode.cn/problems/majority-element/description/)

[TOC]

# 思路

> 既然要找多余一半的，那么就通过记录数量来找最多的

# 解题方法

> 既然答案是多数，那么用少数去抵消多数的票一定剩的还是多数，于是得到多数的答案

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, cnts = inf, 0
        for v in nums:
            if ans == v:
                cnts += 1
            elif not cnts:
                ans = v
            else:
                cnts -= 1
        return ans
```
```Go []
func majorityElement(nums []int) (ans int) {
    cnts := 0
    for _, v := range nums {
        if v == ans {
            cnts++
        } else if cnts == 0 {
            ans = v
        } else {
            cnts--
        }
    }
    return
}
```
```C []
int majorityElement(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0, cnts = 0; i < numsSize; i++) {
        if (nums[i] == ans) {
            cnts++;
        } else if (cnts == 0) {
            ans = nums[i];
        } else {
            cnts--;
        }
    }
    return ans;
}
```
  

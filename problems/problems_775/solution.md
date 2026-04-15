# [Python/Go] 切片递归

> Author: Benhao
> Date: 2022-11-15
> Upvotes: 3
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [775. 全局倒置与局部倒置](https://leetcode.cn/problems/global-and-local-inversions/description/)

[TOC]

# 思路
> 局部倒置的要求其实很苛刻，相邻的逆序对。这个数量是很直观可以统计出的。全局倒置如果要和局部倒置一致，那么他们之间就不能有倒置关系，也就是有某种顺序的存在。再根据题目要求的数目是[0,n-1]进行推理。

# 解题方法
> Python写了一般递归超时了，
```Python3
        # n - 1只能放在最后一个或者倒数第二个，如果放在倒数第二个，最后一个只能放n - 2
        # [ , ... , n - 1, n - 2] 或者 [, ... , n - 1]
        # 如果n - 1在最后一个，那么就是nums去掉最大值的递归, n - 1完全不会参与任何倒置
        return len(nums) <= 1 or (nums[-1] == len(nums) - 1 and self.isIdealPermutation(nums[:-1])) or (nums[-1] == len(nums) - 2 and nums[-2] == len(nums) - 1 and self.isIdealPermutation(nums[:-2]))
```
数组的反复复制递归消耗太大，于是想到了用Go的切片。
其实Py只要不复制数组，直接用坐标递归就可以了(但是就不一行了)


# Code
```Go []

func isIdealPermutation(nums []int) bool {
    return len(nums) <= 1 || (nums[len(nums) - 1] == len(nums) - 1 && isIdealPermutation(nums[:len(nums) - 1])) || (nums[len(nums) - 1] == len(nums) - 2 && nums[len(nums) - 2] == len(nums) - 1 && isIdealPermutation(nums[:len(nums) - 2]))
}
```
```Python3 []
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        def helper(idx):
            return idx <= 1 or (nums[idx] == idx and helper(idx - 1)) or (nums[idx - 1] == idx and nums[idx] == idx - 1 and helper(idx - 2))
        return helper(len(nums) - 1)
```

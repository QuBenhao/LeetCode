# [Python/C] 二分查找

> Author: Benhao
> Date: 2024-04-01
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/)

[TOC]

# 思路

> 题目已给定有序数组，可以二分查找target位置

# 解题方法

> 二分查找

# 复杂度

时间复杂度:
> $O(log_n)$

空间复杂度:
> $O(log_n)$



# Code
```Python3 []
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        return [left, right - 1] if left < len(nums) and nums[left] == target else [-1, -1]
```
```C []
int bisect_left(int *nums, int numsSize, int target) {
    int left = 0, right = numsSize;
    while (left < right) {
        int mid = (right - left) / 2 + left;
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}

int bisect_right(int *nums, int numsSize, int target) {
    int left = 0, right = numsSize;
    while (left < right) {
        int mid = (right - left) / 2 + left;
        if (nums[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int *res = malloc(sizeof(int) * 2);
    *returnSize = 2;
    int left = bisect_left(nums, numsSize, target);
    if (left == numsSize || nums[left] != target) {
        res[0] = -1;
        res[1] = -1;
    } else {
        res[0] = left;
        res[1] = bisect_right(nums, numsSize, target) - 1;
    }
    return res;
}
```

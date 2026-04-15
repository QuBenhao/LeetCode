# [Python/Go/C] fill in largest from back

> Author: Benhao
> Date: 2024-02-21
> Upvotes: 3
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [88. 合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/description/)

[TOC]

# 思路

> Since two array is already sorted, the basic idea comes to mind is to compare the first one of each, and pop the smaller one (pointer move to the right).
But this need a whole array spaces to fill in the ans and copy back to the nums1 array as wanted.
To solve this, we can compare two array from back, and start to fill values at empty part. So the pointers start at back and move to the left. This will fix the extra array and copy back issue.

# 解题方法

> Compare the largest one of each array at time.

# 复杂度

时间复杂度:
> $O(m + n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx, idx1, idx2 = m + n - 1, m - 1, n - 1
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] < nums2[idx2]:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
            else:
                nums1[idx] = nums1[idx1]
                idx1 -= 1
            idx -= 1
        while idx2 >= 0:
            nums1[idx] = nums2[idx2]
            idx -= 1
            idx2 -= 1
```
```Go []
func merge(nums1 []int, m int, nums2 []int, n int)  {
    idx, idx1, idx2 := m + n - 1, m - 1, n - 1
    for ;idx1 >= 0 && idx2 >= 0; idx-- {
        if nums1[idx1] < nums2[idx2] {
            nums1[idx] = nums2[idx2]
            idx2--
        } else {
            nums1[idx] = nums1[idx1]
            idx1--
        }
    }
    for ;idx2 >= 0; idx2-- {
        nums1[idx] = nums2[idx2]
        idx--
    }
}
```
```C []
void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int idx = m + n - 1, idx1 = m - 1, idx2 = n - 1;
    for (; idx1 >= 0 && idx2 >= 0; idx--) {
        nums1[idx] = nums1[idx1] < nums2[idx2] ? nums2[idx2--] : nums1[idx1--];
    }
    for (; idx2 >= 0; idx2--, idx--) {
        nums1[idx] = nums2[idx2];
    }
}
```
  

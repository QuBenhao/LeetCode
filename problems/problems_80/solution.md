# [Python/Go/C] Two pointers

> Author: Benhao
> Date: 2024-02-22
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [80. 删除有序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/)

[TOC]

# Intuition

> Traverse with two pointers

# Approach

> Traverse groups of equal elements from smallest to largest, keeping two copies when duplicates occur.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx, left, right = 0, 0, 0
        while left < len(nums):
            nums[idx] = nums[left]
            idx += 1
            while right < len(nums) and nums[right] == nums[left]:
                right += 1
            if right - left > 1:
                nums[idx] = nums[left]
                idx += 1
            left = right
        return idx
```
```Go []
func removeDuplicates(nums []int) (ans int) {
    for left, right := 0, 0; left < len(nums); left = right {
        nums[ans] = nums[left]
        ans++
        for right < len(nums) && nums[right] == nums[left] {
            right++
        }
        if right - left > 1 {
            nums[ans] = nums[left]
            ans++
        }
    }
    return
}
```
```C []
int removeDuplicates(int* nums, int numsSize) {
    int ans = 0;
    for (int left = 0, right = 0; left < numsSize; left = right) {
        nums[ans++] = nums[left];
        while (right < numsSize && nums[right] == nums[left] && right++ >= 0) {}
        if (right - left > 1) {
            nums[ans++] = nums[left];
        }
    }
    return ans;
}
```
  

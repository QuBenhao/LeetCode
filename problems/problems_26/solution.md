# [Python/Go/C] Advance two pointers

> Author: Benhao
> Date: 2024-02-22
> Upvotes: 5
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/)

[TOC]

# Intuition

> Use the nondecreasing order to find each next distinct element.

# Approach

> Traverse from smallest to largest, finding distinct elements and writing them in order from left to right.

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
        while right < len(nums):
            while right < len(nums) and nums[left] == nums[right]:
                right += 1
            nums[idx] = nums[left]
            idx += 1
            left = right
        return idx
```
```Go []
func removeDuplicates(nums []int) (ans int) {
    for left, right := 0, 0; right < len(nums); left = right {
        nums[ans] = nums[left]
        ans += 1
        for right < len(nums) && nums[right] == nums[left] {
            right++
        }
    }
    return ans
}
```
```C []
int removeDuplicates(int* nums, int numsSize) {
    int ans = 0;
    for (int left = 0, right = 0; right < numsSize; left = right) {
        nums[ans++] = nums[left];
        while (right < numsSize && nums[left] == nums[right] && right++ >= 0) {}
    }
    return ans;
}
```
  

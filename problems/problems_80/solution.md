# [Python/Go/C] 双指针

> Author: Benhao
> Date: 2024-02-22
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [80. 删除有序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/)

[TOC]

# 思路

> 双指针遍历

# 解题方法

> 依次从小到大以相同元素遍历，如果有重复的就保留两个

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  

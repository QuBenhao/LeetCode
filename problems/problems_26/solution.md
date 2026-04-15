# [Python/Go/C] 双指针推移

> Author: Benhao
> Date: 2024-02-22
> Upvotes: 5
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/)

[TOC]

# 思路

> 利用非递减性质，依次找到下一个不重复的元素

# 解题方法

> 遍历从小到大依次找不重复的元素，将他们从左到右按顺序填入

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
  

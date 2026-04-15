# [Python/Go/C] swap with last position

> Author: Benhao
> Date: 2024-02-21
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [27. 移除元素](https://leetcode.cn/problems/remove-element/description/)

[TOC]

# 思路

> Swap to the last available position if left pointer's value is the val to be removed.

# 解题方法

> If the left pointer's value should not be removed, keep moving it to the right. Otherwise, swap its value with the last available position and make the total length minus one. Keep doing so until the left pointer meets the right pointer.

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        left = 0
        while length > 0 and left < length:
            if nums[left] == val:
                nums[left], nums[length - 1] = nums[length - 1], nums[left]
                length -= 1
            else:
                left += 1
        return length
```
```Go []
func removeElement(nums []int, val int) int {
    left, right := 0, len(nums)
    for right > 0 && left < right {
        if nums[left] == val {
            nums[left], nums[right - 1] = nums[right - 1], nums[left]
            right--
        } else {
            left++
        }
    }
    return right
}
```
```C []
int removeElement(int* nums, int numsSize, int val) {
    int left = 0;
    while (left < numsSize) {
        if (nums[left] == val) {
            int tmp = nums[--numsSize];
            nums[numsSize] = nums[left];
            nums[left] = tmp;
        } else {
            left++;
        }
    }
    return numsSize;
}
```
  

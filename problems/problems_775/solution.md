# [Python/Go] Recursion with slices

> Author: Benhao
> Date: 2022-11-15
> Upvotes: 3
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [775. 全局倒置与局部倒置](https://leetcode.cn/problems/global-and-local-inversions/description/)

[TOC]

# Intuition
> A local inversion is strictly defined as an inversion between adjacent elements, so its count is straightforward. For global and local inversion counts to match, there can be no inversions between nonadjacent elements, which implies a certain ordering. Reason from the constraint that the values are [0,n-1].

# Approach
> A straightforward recursive Python solution timed out.
```Python3
        # n - 1 can only be last or second to last; if it is second to last, the last value must be n - 2
        # [ , ... , n - 1, n - 2] or [, ... , n - 1]
        # If n - 1 is last, recurse on nums without its maximum; n - 1 participates in no inversions
        return len(nums) <= 1 or (nums[-1] == len(nums) - 1 and self.isIdealPermutation(nums[:-1])) or (nums[-1] == len(nums) - 2 and nums[-2] == len(nums) - 1 and self.isIdealPermutation(nums[:-2]))
```
Repeatedly copying the array during recursion is too expensive, which led me to Go slices.
Python can also recurse on indices without copying the array (but then it is no longer a one-liner)


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

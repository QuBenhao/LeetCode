# [Python/Go/C] Majority voting

> Author: Benhao
> Date: 2024-02-23
> Upvotes: 28
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [169. 多数元素](https://leetcode.cn/problems/majority-element/description/)

[TOC]

# Intuition

> Since we need the element that occurs more than half the time, track counts to find the most frequent one.

# Approach

> Since the answer is a majority, canceling its votes with minority votes must still leave the majority, giving the answer.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
  

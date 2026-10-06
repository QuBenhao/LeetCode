# [Python/Go/C] Simulation

> Author: Benhao
> Date: 2024-02-24
> Upvotes: 3
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [55. 跳跃游戏](https://leetcode.cn/problems/jump-game/description/)

[TOC]

# Intuition

> Keep updating the farthest reachable distance.

# Approach

> If the farthest distance falls short of the endpoint, return False; otherwise, return True.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = 0
        for i, num in enumerate(nums):
            if i <= cur:
                cur = max(cur, i + num)
                if cur >= len(nums) - 1:
                    return True
            else:
                break
        return False
```
```Go []
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
func canJump(nums []int) bool {
    cur := 0
    for i, v := range nums {
        if i > cur {
            break
        } else {
            cur = max(cur, i + v)
            if cur >= len(nums) - 1 {
                return true
            }
        }
    }
    return false
}
```
```C []
#define MAX(a, b) ((a) < (b) ? (b) : (a))
bool canJump(int* nums, int numsSize) {
    for (int i = 0, cur = 0; i < numsSize; i++) {
        if (i <= cur) {
            cur = MAX(cur, i + nums[i]);
            if (cur >= numsSize - 1) {
                return true;
            }
        } else {
            break;
        }
    }
    return false;
}
```

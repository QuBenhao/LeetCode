# [Python/Go/C] Dynamically update the farthest distance

> Author: Benhao
> Date: 2024-02-25
> Upvotes: 3
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [45. 跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/description/)

[TOC]

# Intuition

> Since the problem guarantees the endpoint is reachable and asks only for the minimum number of jumps, this is the minimum number of updates in problem 55, Jump Game. To reduce updates, after finding the farthest reachable distance, find the next farthest distance within the next interval and count that as one update.

# Approach

> Traverse and update the farthest distance, counting the minimum number of updates.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        cur, nxt = 0, 0
        while nxt < len(nums) - 1:
            ans += 1
            tmp = nxt
            for nx in range(cur, nxt + 1):
                tmp = max(tmp, nx + nums[nx])
            cur, nxt = nxt + 1, tmp
        return ans
```
```Go []
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
func jump(nums []int) (ans int) {
    for cur, nxt, n := 0, 0, len(nums); nxt < n - 1; {
        ans++
        tmp := nxt
        for i := cur; i < nxt + 1; i++ {
            tmp = max(tmp, i + nums[i])
        }
        cur = nxt + 1
        nxt = tmp
    }
    return
}
```
```C []
#define MAX(a, b) ((a) < (b) ? (b) : (a))
int jump(int* nums, int numsSize) {
    int ans = 0;
    for (int cur = 0, nxt = 0; nxt < numsSize - 1; ) {
        ans++;
        int tmp = nxt;
        for (int i = cur; i < nxt + 1; i++) {
            tmp = MAX(tmp, i + nums[i]);
        }
        cur = nxt + 1;
        nxt = tmp;
    }
    return ans;
}
```
  

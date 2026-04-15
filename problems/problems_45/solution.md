# [Python/Go/C] 动态更新最远距离

> Author: Benhao
> Date: 2024-02-25
> Upvotes: 3
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [45. 跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/description/)

[TOC]

# 思路

> 既然题目保证可以到达终点，只是统计最小的跳跃次数，其实就是55跳跃游戏的最少更新次数。怎样减少更新次数呢？每次更新最远距离后，在下一个区间内找下一个最远距离，算一次更新即可。

# 解题方法

> 遍历更新最远距离，统计最小更新次数

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  

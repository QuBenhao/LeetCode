# [Python] Sliding window

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 4
> Tags: C, Go, Java, Python, Python3, TypeScript

---


> Problem: [209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/description/)

[TOC]

# Intuition

> The problem asks for a subarray, not a subsequence. Since the sum covers contiguous elements, a sliding window is the best way to find the minimum window length.

# Approach

> Maintain the window and its sum. Once the requirement is met, remove unnecessary elements from the left and compare window lengths.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans, cur = inf, 0
        window = deque([])
        for num in nums:
            cur += num
            window.append(num)
            while cur >= target:
                ans = min(ans, len(window))
                cur -= window.popleft()
        return ans if ans != inf else 0
```
  

# [Python] Greedy - arithmetic-series sum

> slug: python-tan-xin-shu-xue-deng-chai-shu-lie-ctsg
> date: 2023-11-15
> tags: Greedy, Python3
> question: Maximum Sum With Exactly K Elements  (maximum-sum-with-exactly-k-elements)
> url: https://leetcode.cn/problems/maximum-sum-with-exactly-k-elements/solutions/Jofgro/python-tan-xin-shu-xue-deng-chai-shu-lie-ctsg/

---
(First term + last term) times the number of terms, divided by 2.

# Code
```Python3 []

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return (max(nums) * 2 + k - 1) * k // 2
```

# [Python] Simulation

> slug: python-mo-ni-by-himymben-3cer
> date: 2022-10-24
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Partition Array into Disjoint Intervals (partition-array-into-disjoint-intervals)
> url: https://leetcode.cn/problems/partition-array-into-disjoint-intervals/solutions/44NCiD/python-mo-ni-by-himymben-3cer/

---
### Approach
Find a split where the maximum on the left is no greater than the minimum on the right: compute maxima from left to right and minima from right to left

### Code

```python3
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        maxs, mins = [-1] * n, [inf] * n
        for i, num in enumerate(nums):
            maxs[i] = max(maxs[i - 1], num)
        for i in range(n - 1, -1, -1):
            mins[i] = min(mins[i + 1] if i < n -1 else inf, nums[i])
        for i in range(1, n):
            if maxs[i - 1] <= mins[i]:
                return i
        return -1

```

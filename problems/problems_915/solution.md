# [Python] 模拟

> slug: python-mo-ni-by-himymben-3cer
> date: 2022-10-24
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Partition Array into Disjoint Intervals (partition-array-into-disjoint-intervals)
> url: https://leetcode.cn/problems/partition-array-into-disjoint-intervals/solutions/44NCiD/python-mo-ni-by-himymben-3cer/

---
### 解题思路
找左边最大值比右边最小值的割点，从左往右统计最大值，从右往左统计最小值即可

### 代码

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
# [Python] 模拟

> slug: python-by-himymben-vwrb
> date: 2022-03-13
> tags: Python, Python3
> question: Rank Transform of an Array (rank-transform-of-an-array)
> url: https://leetcode.cn/problems/rank-transform-of-an-array/solutions/InDIeC/python-by-himymben-vwrb/

---
### 代码

```python3
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        return [d[num] for num in arr] if (d := {num: i for i, num in enumerate(sorted(set(arr)), 1)}) else []
```
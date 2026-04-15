# [Python] 贪心

> Author: Benhao
> Date: 2021-07-18
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
能爬到就往上爬，不能爬到就搭梯子直到足够爬到下一个地方

### 代码

```python3
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        cur = ans = 0
        for h in rungs:
            ans += (h - cur - 1) // dist
            cur = h
        return ans
```
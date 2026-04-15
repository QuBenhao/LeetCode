# [Python] 二分法

> Author: Benhao
> Date: 2021-07-11
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
和昨天一样只不过是正序排列了所以用n-mid

### 代码

```python3
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n
        while l < r:
            mid = l + r + 1 >> 1
            if citations[n - mid] >= mid:
                l = mid
            else:
                r = mid - 1
        return l
```
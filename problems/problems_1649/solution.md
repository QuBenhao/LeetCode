# [Python]  有序列表

> Author: Benhao
> Date: 2021-06-22
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
题目很容易看出需要模拟实现每次计算左右两边的数的个数(排序好后左右两边的坐标距离),
使用有序列表可以每个数可以o(logn)二分查找所在位置, o(logn)插入，整体就是o(n * logn)

### 代码

```python3
from sortedcontainers import SortedList


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        pq = SortedList([])
        ans = 0
        for i in instructions:
            ans = (ans + min(pq.bisect_left(i), len(pq) - pq.bisect_right(i))) % (10 ** 9 + 7)
            pq.add(i)
        return ans
```
# [Python] Counter 排序

> Author: Benhao
> Date: 2021-07-03
> Upvotes: 12
> Tags: Python, Python3

---

### 解题思路
按个数排序，个数多的排在前面，然后循环生成即可。

### 代码

```python3
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return "".join(v for v in sorted(c.keys(), key=lambda x:-c[x]) for i in range(c[v]))
```
# [Python] 使用itertools的combinations和product

> Author: Benhao
> Date: 2021-06-21
> Upvotes: 7
> Tags: Python, Python3

---

### 解题思路
小时的位置对应4个灯`1,2,4,8`，所以亮n个灯的所有情况为Combinations([1,2,4,8], n).
分钟的位置对应6个灯`1,2,4,8,16,32`, 所以亮n个灯的情况为Combinations([1,2,4,8,16,32], n).
<br>
我们要找一共有turnedOn个灯的情况，那么必然是小时亮了`i`个灯, 分钟亮了`turnedOn - i`个灯。
再用product遍历当前两者的选择的所有可能组合即可。

### 代码

```python3
from itertools import combinations,product


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for i in range(min(turnedOn + 1, 4)):
            res += [''.join(p) for p in product(self.hours(i), self.minutes(turnedOn - i))]
        return res

    @lru_cache(None)
    def hours(self, n):
        if not n:
            return ["0:"]
        return [str(s) + ':' for i in combinations([1, 2, 4, 8], n) if (s := sum(i)) < 12]

    @lru_cache(None)
    def minutes(self, n):
        if not n:
            return ["00"]
        return [str(s).rjust(2, '0') for i in combinations([1, 2, 4, 8, 16, 32], n) if (s := sum(i)) < 60]
```
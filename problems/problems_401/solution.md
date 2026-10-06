# [Python] Use combinations and product from itertools

> Author: Benhao
> Date: 2021-06-21
> Upvotes: 7
> Tags: Python, Python3

---

### Approach
The hour uses four lights, `1,2,4,8`, so the ways to light n of them are Combinations([1,2,4,8], n).
The minute uses six lights, `1,2,4,8,16,32`, so the ways to light n of them are Combinations([1,2,4,8,16,32], n).
<br>
For a total of turnedOn lights, the hour must use `i` lights and the minute `turnedOn - i` lights.
Use product to enumerate every combination of the current hour and minute choices.

### Code

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

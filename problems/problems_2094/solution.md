# [Python] 暴力枚举符合的排列组合

> Author: Benhao
> Date: 2021-12-05
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
itertools.permutations

### 代码

```python3
from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        for a,b,c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                ans.add(a * 100 + b * 10 + c)
        return list(sorted(ans))
```
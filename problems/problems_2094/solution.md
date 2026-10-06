# [Python] Brute-force enumeration of valid arrangements

> Author: Benhao
> Date: 2021-12-05
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
itertools.permutations

### Code

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

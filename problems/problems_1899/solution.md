# [Python] Greedy with ceilings

> Author: Benhao
> Date: 2021-06-13
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
Imagine three buildings with maximum heights given by target.
Any triplet exceeding a ceiling cannot participate: once a value exceeds the ceiling, it cannot be reduced.
All remaining triplets lie at or below each ceiling. Check only whether each ceiling can be reached; merging all usable triplets gives the maximum at each position.

### Code

```python3
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z = target
        x_ = y_ = z_ = False
        for a,b,c in list(triplets):
            if a > x or b > y or c > z:
                continue
            if a == x:
                x_ = True
            if b == y:
                y_ = True
            if c == z:
                z_ = True
        return x_ and y_ and z_
```

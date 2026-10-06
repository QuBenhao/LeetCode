# [Python] Difference array

> Author: Benhao
> Date: 2021-07-24
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
A difference array adds each color over its interval, then identifies intervals with the same resulting color sum.
Also,
this implementation may be cumbersome: equal color sums need an extra check for boundaries arising from different intervals.

### Code

```python3
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        diff = [0] * 100005
        points = set()
        right = 0
        for a, b, c in segments:
            diff[a] += c
            diff[b] -= c
            right = max(right, b)
            points.add(a)
            points.add(b)
        ans = []
        curr = 0
        left = None
        color = 0
        for i in range(1, right + 1):
            curr += diff[i]
            if color and curr != color:
                if color and left is not None:
                    ans.append([left, i, color])
                if curr:
                    left = i
                    color = curr
                else:
                    left = None
            elif color and curr == color:
                if i in points and left is not None:
                    ans.append([left, i, color])
                    left = i
            if curr and left is None:
                left = i
                color = curr
        return ans
```

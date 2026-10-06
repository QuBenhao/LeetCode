# [Python] Binary search packages by box size

> Author: Benhao
> Date: 2021-06-06
> Upvotes: 5
> Tags: Python, Python3

---

### Approach
I'm an idiot.

### Code

```python3
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        ans = float("inf")
        for box in boxes:
            box.sort()
            if packages[-1] > box[-1]:
                continue
            idx = 0
            curr = 0
            for b in box:
                last = idx
                idx = bisect.bisect_right(packages, b, lo=last)
                # We need (idx-last) boxes of size b
                curr += (idx - last) * b
            ans = min(ans, curr)
        return (ans-sum(packages)) % (10 ** 9 + 7) if ans != float("inf") else -1
```

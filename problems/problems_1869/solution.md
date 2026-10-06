# [Python] Split the string into runs of 0s and 1s

> Author: Benhao
> Date: 2021-05-23
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Split on runs of 0s to get the lengths of all runs of 1s, and vice versa.
Compare the maximum lengths.

### Code

```python3
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        l1 = re.split("0+", s)
        l0 = re.split("1+", s)
        return len(max(l1, key=len)) > len(max(l0, key=len))
```

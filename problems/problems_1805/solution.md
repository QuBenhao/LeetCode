# [Python] Count distinct integers with a set

> Author: Benhao
> Date: 2021-03-28
> Upvotes: 2
> Tags: Python

---

### Approach
Write the solution approach here

### Code

```python
class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        ans = set()
        last = None
        for c in word + "#":
            if '0' <= c <= '9':
                if last is None:
                    last = int(c)
                else:
                    last *= 10
                    last += int(c)
            elif last is not None:
                ans.add(last)
                last = None
        return len(ans)
```

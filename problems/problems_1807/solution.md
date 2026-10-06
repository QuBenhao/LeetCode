# [Python] Build a dictionary, then look up each key

> Author: Benhao
> Date: 2021-03-28
> Upvotes: 2
> Tags: Python

---

### Approach
A straightforward approach.

### Code

```python
class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d = dict()
        for k,v in knowledge:
            d[k] = v
        ans = ""
        isKey = False
        key = ""
        for c in s:
            if c == '(':
                isKey = True
            elif c == ')':
                isKey = False
                if key in d:
                    ans += d[key]
                else:
                    ans += '?'
                key = ""
            elif not isKey:
                ans += c
            else:
                key += c
        return ans

```

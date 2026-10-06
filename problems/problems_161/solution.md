# [Python] Brute force

> slug: python-bao-li-by-himymben-ddol
> date: 2021-08-21
> tags: Python, Python3
> question: One Edit Distance (one-edit-distance)
> url: https://leetcode.cn/problems/one-edit-distance/solutions/nUXvoS/python-bao-li-by-himymben-ddol/

---
### Approach
The strings must become equal after exactly one edit.

### Code

```python3
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        if abs(len_s - len_t) > 1 or s == t:
            return False
        elif len_s == len_t:
            return sum(s[i] != t[i] for i in range(len_s)) <= 1
        if len_s < len_t:
            s, t = t, s
        return any(s[:i] + s[i+1:] == t for i in range(len(s)))
```

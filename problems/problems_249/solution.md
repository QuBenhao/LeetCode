# [Python] Custom hash algorithm

> slug: python-zi-ding-yi-ha-xi-suan-fa-by-himym-rebw
> date: 2021-08-22
> tags: Python, Python3
> question: Group Shifted Strings (group-shifted-strings)
> url: https://leetcode.cn/problems/group-shifted-strings/solutions/kYJJCr/python-zi-ding-yi-ha-xi-suan-fa-by-himym-rebw/

---
### Approach
Strings related by shifting must have matching differences between corresponding character positions.

### Code

```python3
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # Strings can be shifted into each other only when the differences at corresponding positions match
        def hashCounter(string):
            return tuple(((ord(string[i]) - ord(string[i-1])) % 26) for i in range(1 , len(string))) if len(string) > 1 else 0

        ans = defaultdict(list)
        for s in strings:
            ans[hashCounter(s)].append(s)
        return list(ans.values())
```

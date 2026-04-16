# [Python] 贪心

> Author: Benhao
> Date: 2021-07-26
> Upvotes: 1
> Tags: Python, Python3

---

```python3
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        ans = []
        changed = False
        for i,c in enumerate(num):
            t = int(c)
            if change[t] > t:
                changed = True
                ans.append(str(change[t]))
            elif change[t] == t:
                ans.append(c)
            else:
                if changed:
                    ans.append(num[i:])
                    break
                ans.append(c)
        return ''.join(ans)
```
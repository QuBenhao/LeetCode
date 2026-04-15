# [Python] 集合统计整数

> Author: Benhao
> Date: 2021-03-28
> Upvotes: 2
> Tags: Python

---

### 解题思路
此处撰写解题思路

### 代码

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
# [Python] 先生成字典，再遍历调用key

> Author: Benhao
> Date: 2021-03-28
> Upvotes: 2
> Tags: Python

---

### 解题思路
很直接的思路

### 代码

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
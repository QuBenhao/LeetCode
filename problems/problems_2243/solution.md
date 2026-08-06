# [Python] 模拟

> slug: python-mo-ni-by-himymben-jc5a
> date: 2022-04-17
> tags: Python, Python3
> question: Calculate Digit Sum of a String (calculate-digit-sum-of-a-string)
> url: https://leetcode.cn/problems/calculate-digit-sum-of-a-string/solutions/vSK8ph/python-mo-ni-by-himymben-jc5a/

---
### 解题思路
该用户太懒了只有代码

### 代码

```python3
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            nxt, cur, num = [], 0, 0
            for i, c in enumerate(s):
                cur += 1
                if cur > k:
                    nxt.append(str(num))
                    cur, num = 1, 0
                num += ord(c) - ord('0')
            if cur:
                nxt.append(str(num))
            s = "".join(nxt)
        return s
```
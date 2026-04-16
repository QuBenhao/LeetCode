# [Python] 贪心

> Author: Benhao
> Date: 2021-05-30
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
首先x这个数是必须加入整个字符串的。
那么负数的时候，我们遇到一个比x大的数（字符），x插在这里会比x插在后面任意地方的结果都大。
而正数的时候，我们遇到一个比x小的数（字符），x插在这里会比x插在后面任意地方的结果都大。

### 代码

```python3
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0]=='-':
            for i,c in enumerate(n[1:], 1):
                if int(c) > x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        else:
            for i,c in enumerate(n):
                if int(c) < x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
```
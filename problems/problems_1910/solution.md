# [Python] 模拟

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
咋感觉比上一题好写呢

### 代码

```python3
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            idx = s.index(part)
            s = s[:idx] + s[idx+len(part):]
        return s

```
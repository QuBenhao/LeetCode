# [Python] O(n^2)

> Author: Benhao
> Date: 2021-07-11
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
只贴了一段代码

### 代码

```python3
class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        squares = set(i ** 2 for i in range(1, n + 1))
        for i in range(1, n + 1):
            for j in range(1, i):
                if i * i + j * j in squares:
                    ans += 2
        return ans

```
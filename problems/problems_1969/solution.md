# [Python] 贪心一行

> Author: Benhao
> Date: 2021-08-15
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
没工夫证明，看灵老师的吧

### 代码

```python3
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        return (m:=(2 ** p - 1)) * pow(m - 1, m//2, 10 ** 9 + 7) % (10 ** 9 + 7)
```
# [Python] 异或后统计1的个数即可

> Author: Benhao
> Date: 2021-05-27
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
该用户太懒了，只写了一行代码。

### 代码

```python3
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
```
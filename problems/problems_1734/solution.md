# [Python] 双100%，异或找初始值

> Author: Benhao
> Date: 2021-05-10
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
perm[0] 与perm每一个值的异或结果可以由encoded求出。
perm所有值的异或结果可以由1到n的异或结果得出。
由于n是奇数，perm[0]和每一个值的异或的结果的异或，刚好是不带perm[0]的1到n的异或结果。
所以两者的异或就是perm[0]了

### 代码

```python
class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        n = len(encoded) + 1
        # perm[0] = (perm[0] ^ perm[1] ^ ... perm[n-1]) ^ (perm[1] ^ perm[2]) ^ ... ^ (perm[n-2] ^ perm[n-1])
        # perm[0] = 1 ^ encoded[1] ^ encoded[3] ^ ... encoded[n-2] if n % 4 == 1 else encoded[1] ^ encoded[3] ^ ... encoded[n-2]
        start = 0
        for i in range(1, n, 2):
            start ^= encoded[i]
        # 连续n个数的异或结果模4为1时为1，为3时为0
        if n % 4 == 1:
            start ^= 1
        perm = [start]
        for e in encoded:
            perm.append(perm[-1] ^ e)
        return perm
```
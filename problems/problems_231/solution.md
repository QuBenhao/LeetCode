# [Python] 位运算 100%

> Author: Benhao
> Date: 2021-05-29
> Upvotes: 5
> Tags: Python, Python3

---

### 解题思路
使用`x&(-x)==x`或者`x&(x-1)==0`来判断2的幂
> 这是因为x&(-x)会找到x的最右边的二进制位数，如果n等于这个值，说明n的二进制只有这么一个位数，故而必然是2的幂。
> 同样的，2的幂的二进制减一，必然得到一个所有位与当前相反的二进制，他们的与为0说明是2的幂。

### 代码

```python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n == n & (-n) if n else False
```

```python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return not n & (n-1) if n else False
```
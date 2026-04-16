# [Python] 快速幂

> Author: Benhao
> Date: 2021-07-04
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
因为偶数位只能填0,2,4,6,8(允许前缀0)五个数，奇数位只有2,3,5,7四个质数。
所以最终结果就是偶数位的组合数乘上奇数W位组合数

### 代码

```python3
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # 偶数位 0, 2, 4, 6, 8； 奇数位 2, 3, 5, 7
        return (pow(5, ceil(n/2), 10**9+7) * pow(4, n//2, 10**9+7)) % (10**9+7)
```
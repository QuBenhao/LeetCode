# [Python] 费马平方和定理

> Author: Benhao
> Date: 2021-04-28
> Upvotes: 9
> Tags: Python, Python3

---

### 解题思路
根据费马平方和定理，检查所有模4余3的因子的个数是否为偶数个即可

### 代码

```python3
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if not c:
            return True
        # (a - b) ^ 2 + (a + b) ^ 2 = 2 * (a ^ 2 + b ^ 2) = 2 * c
        while c % 2 == 0:
            c //= 2
        # 费马平方和定理
        if c % 4 == 3:
            return False
        sqrt = int(math.sqrt(c))
        for i in range(3, sqrt + 1, 4):
            count = 0
            while c % i == 0:
                c //= i
                count += 1
            if count % 2 != 0:
                return False
        return True
```
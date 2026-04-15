# 懒标记+模逆元

> Author: Benhao
> Date: 2026-03-14
> Upvotes: 2
> Tags: Math, Python3

---


> Problem: [1622. 奇妙序列](https://leetcode.cn/problems/fancy-sequence/description/)

[TOC]

## 方法：懒标记 + 模逆元

### 思路




首先考虑朴素做法：每次 `addAll` 和 `multAll` 都遍历数组进行修改，时间复杂度为 $O(n)$，显然会超时。




我们注意到，`addAll` 和 `multAll` 对数组中所有元素的作用可以统一表示为线性变换：




$$f(x) = \text{mul} \times x + \text{add}$$




因此，我们可以维护两个懒标记 `mul` 和 `add`，将操作延迟到查询时计算。




**懒标记的更新规则：**




- `addAll(inc)`：所有元素加 `inc`，即 `add += inc`

- `multAll(m)`：所有元素乘 `m`，即 `mul *= m, add *= m`




这样两种操作都是 $O(1)$ 时间。




**新元素的处理：**




当调用 `append(val)` 时，当前标记为 $(\text{mul}, \text{add})$。如果直接存储 `val`，后续查询时会重复应用标记。




解决方案是存储元素的**归一化值**，即假设当前标记为 $(1, 0)$ 时该元素的值：




$$\text{stored} = \frac{\text{val} - \text{add}}{\text{mul}}$$




查询时用当前标记还原：




$$\text{result} = \text{mul} \times \text{stored} + \text{add}$$




**模逆元：**




模意义下的除法需要求逆元。由于 $10^9 + 7$ 是质数，根据费马小定理：




$$a^{p-1} \equiv 1 \pmod{p}$$




可得：




$$a^{-1} \equiv a^{p-2} \pmod{p}$$




因此用快速幂即可求逆元。




### 代码

```python [Python3]
MOD = 10 ** 9 + 7

# 费马小定理
def inv(x):
    # py的快速幂
    return pow(x, MOD - 2, MOD)

class Fancy:
    def __init__(self):
        self.mul = 1
        self.add = 0
        self.arr = []

    def append(self, val: int) -> None:
        """
        我们有f(x) = mul * x + add, 那么 f(x) = val时, x = (val - add) / mul
        这里涉及到模逆元，所以用inv(mul)表示除以mul
        翻译一下这里就是 (val - add) / mul的意思
        """
        self.arr.append((val - self.add) * inv(self.mul) % MOD)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % MOD
        self.add = (self.add * m) % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.mul * self.arr[idx] % MOD + self.add) % MOD
```




### 复杂度分析




- 时间复杂度：$O(1)$ 每次 `addAll` 和 `multAll`，$O(\log \text{MOD})$ 每次 `append` 和 `getIndex`。

- 空间复杂度：$O(n)$，其中 $n$ 为 `append` 的调用次数。


  

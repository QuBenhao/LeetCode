# Lazy tags + modular inverse

> Author: Benhao
> Date: 2026-03-14
> Upvotes: 2
> Tags: Math, Python3

---


> Problem: [1622. 奇妙序列](https://leetcode.cn/problems/fancy-sequence/description/)

[TOC]

## Method: lazy tags + modular inverse

### Intuition




The naive approach updates the entire array on every `addAll` and `multAll` call, taking $O(n)$ time per operation and exceeding the time limit.




The effect of `addAll` and `multAll` on every element can be expressed as a linear transformation:




$$f(x) = \text{mul} \times x + \text{add}$$




Maintain two lazy tags, `mul` and `add`, and defer applying them until a query.




**Updating the lazy tags:**




- `addAll(inc)`: add `inc` to every element, so `add += inc`.

- `multAll(m)`: multiply every element by `m`, so `mul *= m, add *= m`.




Both operations now take $O(1)$ time.




**Handling new elements:**




When `append(val)` is called, the current tags are $(\text{mul}, \text{add})$. Storing `val` directly would apply the existing tags again on a later query.




Instead, store the element's **normalized value**: the value it would have if the current tags were $(1, 0)$:




$$\text{stored} = \frac{\text{val} - \text{add}}{\text{mul}}$$




Reconstruct the value with the current tags when querying:




$$\text{result} = \text{mul} \times \text{stored} + \text{add}$$




**Modular inverse:**




Division in modular arithmetic requires a modular inverse. Since $10^9 + 7$ is prime, Fermat's little theorem gives:




$$a^{p-1} \equiv 1 \pmod{p}$$




Therefore:




$$a^{-1} \equiv a^{p-2} \pmod{p}$$




The inverse can thus be computed with fast exponentiation.




### Code

```python [Python3]
MOD = 10 ** 9 + 7

# Fermat's little theorem
def inv(x):
    # Python's fast exponentiation
    return pow(x, MOD - 2, MOD)

class Fancy:
    def __init__(self):
        self.mul = 1
        self.add = 0
        self.arr = []

    def append(self, val: int) -> None:
        """
        Given f(x) = mul * x + add, when f(x) = val, x = (val - add) / mul
        Use the modular inverse inv(mul) to represent division by mul
        In other words, this means (val - add) / mul
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




### Complexity analysis




- Time complexity: $O(1)$ per `addAll` and `multAll`, and $O(\log \text{MOD})$ per `append` and `getIndex`.

- Space complexity: $O(n)$, where $n$ is the number of `append` calls.


  

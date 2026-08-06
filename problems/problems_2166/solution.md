# [Python] 二进制模拟

> slug: python-er-jin-zhi-mo-ni-by-himymben-gw1a
> date: 2022-02-06
> tags: Python, Python3
> question: Design Bitset (design-bitset)
> url: https://leetcode.cn/problems/design-bitset/solutions/tdDjNH/python-er-jin-zhi-mo-ni-by-himymben-gw1a/

---
### 解题思路
用二进制模拟题目的操作

### 代码

```python3
class Bitset:

    def __init__(self, size: int):
        self.num = 0
        self.len = size
        self.total = 0
        self.power = 1 << self.len

    def fix(self, idx: int) -> None:
        idx = self.len - idx - 1
        if not (self.num >> idx) & 1:
            self.total += 1
        self.num |= (1 << idx)

    def unfix(self, idx: int) -> None:
        idx = self.len - idx - 1
        if (self.num >> idx) & 1:
            self.total -= 1
            self.num ^= (1 << idx)

    def flip(self) -> None:
        self.total = self.len - self.total
        self.num = self.power - 1 - self.num

    def all(self) -> bool:
        return self.total == self.len

    def one(self) -> bool:
        return self.total > 0

    def count(self) -> int:
        return self.total

    def toString(self) -> str:
        s = bin(self.num)[2:]
        return "0" * (self.len - len(s)) + s


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
```
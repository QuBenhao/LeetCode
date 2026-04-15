# [Python] Trie字典树

> Author: Benhao
> Date: 2021-05-16
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
字典实现，查询的时候根据当前最大值判断有没有更大的结果存在

### 代码

```python3
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        t = Trie(len(bin(max(nums)))-2)
        for num in nums:
            ans = t.query(num, ans)
            t.insert(num)
        return ans


class Trie:
    def __init__(self, max_bit):
        self.root = {}
        self.max_bit = max_bit
    
    def insert(self, x):
        node = self.root
        for i in range(self.max_bit,-1,-1):
            bit = x >> i & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]
    
    def query(self, x, high):
        node = self.root
        acc = 0
        g = False
        for i in range(self.max_bit,-1,-1):
            acc = acc << 1
            bit = x >> i & 1
            if not g:
                h_bit = high >> i & 1
            if 1 ^ bit in node:
                if not g and not h_bit:
                    g = True
                acc += 1
                node = node[1 ^ bit]
            elif bit in node:
                if not g and h_bit:
                    return high
                node = node[bit]
        return acc

```
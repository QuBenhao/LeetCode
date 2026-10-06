# [Python] Trie

> Author: Benhao
> Date: 2021-05-23
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
This was the last problem in a weekly contest I entered last year, when I barely knew anything. I can finally solve it now.
Sorting the queries lets us insert only eligible numbers. Then greedily maximize the XOR: choose a 1 bit whenever possible, otherwise accept 0. If neither is possible, no number is available; return -1.
Use idx to track how far we have inserted into nums.

### Code

```python3
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        qrs = sorted(enumerate(queries),key=lambda x:x[1][1])
        trie = Trie()
        idx, n = 0, len(nums)
        ans = [0] * len(qrs)
        for i,(x, m) in qrs:
            while idx < n and nums[idx] <= m:
                trie.add(nums[idx])
                idx += 1
            ans[i] = trie.query(x)
        return ans


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, x):
        node = self.root
        for i in range(31, -1, -1):
            bit = x >> i & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def query(self, x):
        res = 0
        node = self.root
        for i in range(31, -1, -1):
            res <<= 1
            bit = x >> i & 1
            xor = bit ^ 1
            if xor in node:
                res += 1
                node = node[xor]
            elif bit in node:
                node = node[bit]
            else:
                return -1
        return res
```

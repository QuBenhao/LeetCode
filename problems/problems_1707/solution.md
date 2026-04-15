# [Python] 前缀树

> Author: Benhao
> Date: 2021-05-23
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
艾玛这不就是去年啥也不会的时候参加的周赛最后一题么。现在终于会了。
排序后查询的意义是我们只加入能使用的num到数组中，这样查找最大值时可以使用贪心，能异或取1就取1，不能再妥协取0，啥也取不了的说明没数，返回-1。
用idx记一下当前插入了的nums的位置。

### 代码

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
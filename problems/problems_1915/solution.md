# [Python] Annotated code

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Based on this [explanation](https://leetcode.cn/problems/number-of-wonderful-substrings/solution/qian-zhui-he-chang-jian-ji-qiao-by-endle-t57t/) and [code](https://leetcode.com/problems/number-of-wonderful-substrings/discuss/1299537/Python3-freq-table-w.-mask)

### Code

```python3
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # At position i, encode the parity of counts for a through j in prefix 0..i using 10 bits: 0 for even, 1 for odd
        # Bitmask of count parities from 0 through i
        ans = mask = 0
        # Count each bitmask seen so far; the empty prefix occurs once
        freq = defaultdict(int, {0:1})
        for c in word:
            # Toggle the current character's count parity
            mask ^= 1 << (ord(c) - 97)
            for i in range(10):
                # Count masks differing only in bit i: the intervening substring has an odd count for character i
                ans += freq[mask ^ 1 << i]
            # Every character appears an even number of times
            ans += freq[mask]
            freq[mask] += 1
        return ans

```

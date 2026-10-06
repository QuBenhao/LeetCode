# [Python] Count zeros and ones at each bit position

> Author: Benhao
> Date: 2021-05-28
> Upvotes: 12
> Tags: Python, Python3

---

### Approach
> First code block
> Use a Counter to record the number of `1`s at each bit position. For each number, compute its Hamming distances from preceding numbers while updating the Counter.

> The second code block removes the per-iteration Hamming-distance calculation. At the end, multiply the count of `0`s by the count of `1`s at each position. This replaces `repeated addition` with `a sum of products`.
> The count of `0`s at a position is the total number count minus the count of `1`s.

> From the second code block, it is easy to see:
> We need only the counts of `0`s and `1`s at each position, similar to yesterday's use of bin(x).count('1').
> Use `map` + `bin` to obtain every number's binary string, then count '1's at each position. Transposing with `zip` does exactly this.
> Use 30 bits because 2^29 < 10^9 < 2^30.

**About format**
Convert decimal values to a fixed-width representation in another base:
> `8-bit binary`
> '{:08b}'.format(9)
> '00001001'

> `6-digit octal`
> '{:06o}'.format(9)
> '000011'

>`6-digit hexadecimal`
> '{:06x}'.format(9)
> '000009'


### Code

```python3
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        trie = Counter()
        max_bit = len(bin(max(nums))) - 2
        ans = 0
        for i, num in enumerate(nums):
            for j in range(max_bit):
                bit = (num >> j) & 1
                if bit:
                    ans += i - trie[j]
                    trie[j] += 1
                else:
                    ans += trie[j]
        return ans
```

```python3
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        trie = Counter()
        max_bit = len(bin(max(nums))) - 2
        n = len(nums)
        for i, num in enumerate(nums):
            for j in range(max_bit):
                if (num >> j) & 1:
                    trie[j] += 1
        return sum(trie[i] * (n - trie[i]) for i in range(max_bit))
```

```python3
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        return sum((ones:= s.count('1')) * (len(nums) - ones) for s in zip(*map('{:30b}'.format, nums)))
```

# [Python] Count with a hash table

> Author: Benhao
> Date: 2021-07-07
> Upvotes: 7
> Tags: Python, Python3

---

### Approach
Build a Counter, then for each number enumerate powers of two from $2^0$ through $2^{21}$. Multiply that number's count by the count of the power of two minus that number to count pairs summing to the power of two.
When a number is half a power of two, pairs of equal values use the combination formula for choosing two from n.

Divide the final result by 2 because each pair is counted twice.

<br>
An incremental approach that avoids double counting is also included.

### Code

```python3
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnts = Counter(deliciousness)
        return (sum(cnts[key] * (cnts[key] - 1) if key == 2 ** (i-1) else cnts[key] * cnts[2**i-key] for key in cnts for i in range(22))//2) % (10 ** 9 + 7)
```
These two snippets are equivalent; the first is simply written on one line.
```python3
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnts = Counter(deliciousness)
        ans = 0
        for key in cnts:
            for i in range(22):
                if key == 2 ** (i-1):
                    ans += cnts[key] * (cnts[key] - 1)
                else:
                    ans += cnts[key] * cnts[2**i - key]
        return (ans // 2) % (10 ** 9 + 7)
```
Avoid recomputing the 22 powers of two to speed this up. Starting the loop near the key's value can also help.
```python3
class Solution:
    powersOfTwo = [2**i for i in range(22)]
    mod = 10 ** 9 + 7

    def countPairs(self, deliciousness: List[int]) -> int:
        cnts = Counter(deliciousness)
        return (sum(cnts[key] * (cnts[key] - 1) if key == target - key else cnts[key] * cnts[target-key] for key in cnts for target in self.powersOfTwo))//2 % self.mod
```
Incremental counting
```python3
class Solution:
    powersOfTwo = [2**i for i in range(22)]
    mod = 10 ** 9 + 7

    def countPairs(self, deliciousness: List[int]) -> int:
        cnts, ans = Counter(), 0
        for num in deliciousness:
            for target in self.powersOfTwo:
                ans += cnts[target - num]
            cnts[num] += 1
        return ans % self.mod
```
Advanced 100% solution, based on an idea from [@DarkArmed](/u/darkarmed/)
```python3
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 1000000007
        count = Counter(deliciousness)

        res = 0
        # Each number considers only pairs summing to its next power of two, avoiding duplicates: 1+3=4 is counted only at 3, and 3+5=8 only at 5
        for i in count:
            if i == 0:
                continue
            # The next power of two after i
            target = self.nextPower(i)
            # If i can combine with a key in count to reach this power
            res += count[i] * count[target - i]
            # If i itself is a power of two
            if i == target:
                res += count[i] * (count[i] - 1) // 2
        return res % MOD

    def nextPower(self, x: int):
        x -= 1
        x |= x >> 1
        x |= x >> 2
        x |= x >> 4
        x |= x >> 8
        x |= x >> 16
        return x + 1
```

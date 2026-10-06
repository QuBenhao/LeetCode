# [Python] Prefix mismatch counts for 01 and 10 patterns

> Author: Benhao
> Date: 2021-06-06
> Upvotes: 6
> Tags: Python, Python3

---

### Approach
pre01[i+1] counts mismatches between positions 0 through i and the 010101 pattern. The other prefix array works similarly.

For even n, both parts must follow either 1010 or 0101, so return the smaller mismatch count.
For odd n, enumerate the operation count for moving each possible prefix length to the end.

### Code

```python3
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        pre01 = [0] * n
        pre10 = [0] * n
        for i,c in enumerate(s):
            if c == '1':
                if i % 2 == 0:
                    pre01[i] = pre01[i-1] + 1
                    pre10[i] = pre10[i-1]
                else:
                    pre10[i] += pre10[i-1] + 1
                    pre01[i] = pre01[i-1]
            else:
                if i % 2 == 0:
                    pre10[i] += pre10[i-1] + 1
                    pre01[i] = pre01[i-1]
                else:
                    pre01[i] = pre01[i-1] + 1
                    pre10[i] = pre10[i-1]
        pre01 = [0] + pre01
        pre10 = [0] + pre10
        if n % 2 == 0:
            return min(pre01[-1],pre10[-1])
        ans = float("inf")
        for i in range(n):
            # Move the first i characters to the end
            # The front needs 10101 and the back needs 010
            ans1 = pre01[-1] - pre01[i] + pre10[i]
            ans2 = pre10[-1] - pre10[i] + pre01[i]
            ans = min(ans, ans1, ans2)
        return ans
```

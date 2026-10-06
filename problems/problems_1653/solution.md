# [Python] Prefix counts at every split, or dynamic programming

> Author: Benhao
> Date: 2021-06-04
> Upvotes: 6
> Tags: Python, Python3

---

### Approach
**Brute force with prefix counts**
For each split, keep only 'a' on the left and 'b' on the right. Count the 'b' characters to delete on the left and the 'a' characters to delete on the right.
Use prefix sums to count 'a' characters; the 'b' count is the length minus the 'a' count.
Compute the deletions needed at each split and return the minimum.

**Dynamic programming**
Assume the preceding string is balanced: it either ends with 'b' or consists entirely of 'a' characters.
If the current character is 'b', it preserves the balance.
If the current character is 'a',
either keep it and delete every preceding 'b',
or delete it and preserve the preceding string's balance.

The optimum at this position is therefore the smaller of `the previous optimum + 1` and `the number of b characters`.

### Code

```python3
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        count = [0] * (n + 1)
        for i,c in enumerate(s):
            if c == 'a':
                count[i+1] = count[i] + 1
            else:
                count[i+1] = count[i]
        ans = float("inf")
        for i in range(n):
            # Count 'b' characters through i and 'a' characters after i
            b = i - count[i]
            a = count[-1] - count[i+1]
            if not a and not b:
                return 0
            ans = min(ans, b+a)
        return ans
```

```python3
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Number of b characters
        cnt = ans = 0
        for c in s:
            if c == 'b':
                # Ending with 'b' preserves the previous balance
                cnt += 1
            else:
                # For a final 'a', either delete it after balancing the prefix or delete all preceding 'b' characters
                ans = min(ans + 1, cnt)
        return ans
```

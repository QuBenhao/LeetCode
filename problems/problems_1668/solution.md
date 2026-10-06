# [Python] Repeated string matching or dynamic programming

> Author: Benhao
> Date: 2021-05-26
> Upvotes: 4
> Tags: Python, Python3

---

### Approach
> Repeated matching
> Starting with `k` = 1, whenever `k` copies of word match, try `k+1` copies. Stop when they no longer match.

> Dynamic programming
> Whenever word matches at the current position, update the maximum at the position immediately after it.


### Code

```python3
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans, match = 0, word
        while sequence.find(match) != -1:
            ans += 1
            match += word
        return ans

```

```python3
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        m, n = len(sequence), len(word)
        dp = [0] * m
        for i,c in enumerate(sequence):
            if c == word[0] and sequence[i:i+n] == word:
                dp[i + n - 1] = max(dp[i - 1] + 1, dp[i+n-1])
        return max(dp)
```

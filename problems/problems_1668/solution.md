# [Python] 叠加匹配字符串 or 动态规划

> Author: Benhao
> Date: 2021-05-26
> Upvotes: 4
> Tags: Python, Python3

---

### 解题思路
> 叠加匹配
> 每匹配到一次`k`个word,尝试匹配`k+1`个word，直到匹配不了为止。`k`从1开始。

> 动态规划
> 每从当前位置匹配到一个word，更新word后位置的最大值


### 代码

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
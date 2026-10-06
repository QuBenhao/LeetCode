# [Python] DP with O(m*n) time and O(n) space

> Author: Benhao
> Date: 2021-03-17
> Upvotes: 3
> Tags: Python

---

### Approach
Simplified from an approach with O(m*n) space complexity.

```python
        dp = [[1] * (m + 1)] + [[0] * (m + 1) for _ in range(n)]

        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] += dp[i + 1][j]
                if t[i] == s[j]:
                    dp[i + 1][j + 1] += dp[i][j]
```
`dp[i][j]` represents the result of numDistinct(s[:j],t[:i]).
Any occurrence of t[:i+1] in s[:j] is still present after adding one character to s, so `dp[i+1][j+1] += dp[i+1][j]`.
If `s[j] == t[i]`, the preceding s[:j] does not need to include the character at index i of t, so `dp[i+1][j+1] += dp[i][j]`.
<br>
To reduce the two-dimensional DP to one dimension, keep the value in the corresponding column for each row and update it incrementally.
At each step, the stored values correspond to the current column: dp[:][j] for s[:j]. They count how many times each corresponding t[:i+1] occurs as a subsequence of s from index 0 through j-1.
<br>
For example, with `s="babgbag"` and `t="bag"`:
During the loop:
i = 0, the first column is initialized to [1, 0, 0, 0]
i = 1, in the second column, s[0] == t[0], so the array becomes [1, 1, 0, 0] (dp[1] += dp[0])
i = 2, in the third column, s[1] == t[1], so the array becomes [1, 1, 1, 0] (dp[2] += dp[1])
i = 3, in the fourth column, s[2] == t[0], so the array becomes [1, 2, 1, 0] (dp[1] += dp[0])
i = 4, in the fifth column, s[3] == t[2], so the array becomes [1, 2, 1, 1] (dp[3] += dp[2])
i = 5, in the sixth column, s[4] == t[0], so the array becomes [1, 3, 1, 1] (dp[1] += dp[0])
i = 6, in the seventh column, s[5] == t[1], so the array becomes [1, 3, 4, 1] (dp[2] += dp[1])
i = 7, in the eighth column, s[6] == t[2], so the array becomes [1, 3, 4, 5] (dp[3] += dp[2])
The loop ends with a result of 5.
<br>
In the example above, t has no repeated characters.
For example, with `s="rabbb"` and `t="bb"`:
i = 0, dp = [1, 0, 0]
i = 1, dp = [1, 0, 0]
i = 2, dp = [1, 0, 0]
i = 3, dp = [1, 1, 0] (dp[2] += dp[1], dp[1] += dp[0]) because "rab" contains "b" once as a subsequence, but cannot contain "bb"
i = 4, dp = [1, 2, 1] (dp[2] += dp[1], dp[1] += dp[0]) because the preceding "rab" already contains "b" once, and adding another "b" creates one occurrence of "bb". The new "b" also adds another occurrence of "b".
i = 5, dp = [1, 3, 3] (dp[2] += dp[1], dp[1] += dp[0])
<br>
As this shows, **reverse iteration ensures that, for each t[:i+1], we use only the count of t[:i] from the previous iteration**.

*Note: i and j in the code below are swapped relative to the explanation above.*

### Code

```python
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)

        dp = [1] + [0] * n

        for i in range(1, m + 1):
            for j in range(min(i,n), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]

```

# [Python] Dynamic programming in four lines

> Author: Benhao
> Date: 2021-08-01
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
A 0 can extend every earlier all-zero subsequence or form one by itself, so `dp[0] += dp[0] + 1`.
A 1 can extend every all-zero subsequence or every valid subsequence ending in 1, so `dp[1] += dp[0] + dp[1]`.
The transition for 2 is analogous.
Return dp[2].

### Code

```python3
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp = [0, 0, 0, 1]
        for num in nums:
            dp[num] += dp[num - 1] + dp[num]
        return dp[2] % (10 ** 9 + 7)
```
Large integers slow computation; applying the modulus earlier speeds it up.
```python3
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp, mod = [0, 0, 0, 1], 10 ** 9 + 7
        for num in nums:
            dp[num] = (2 * dp[num] + dp[num - 1]) % mod
        return dp[2]
```

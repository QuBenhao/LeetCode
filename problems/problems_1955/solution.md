# [Python] 动态规划(四行代码)

> Author: Benhao
> Date: 2021-08-01
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
0能和前面所有的0的序列组成全是0的序列，也包括它自己单独成为一个。所以`dp[0] += dp[0] + 1`；
1能和前面所有的0的序列组成以1结尾的序列，也可以和前面以1结尾的序列。所以`dp[1] += dp[0] + dp[1]`
2和1同理。
最后返回dp[2]即可。

### 代码

```python3
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp = [0, 0, 0, 1]
        for num in nums:
            dp[num] += dp[num - 1] + dp[num]
        return dp[2] % (10 ** 9 + 7)
```
数字大计算比较慢，把取余移上去可以加速
```python3
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp, mod = [0, 0, 0, 1], 10 ** 9 + 7
        for num in nums:
            dp[num] = (2 * dp[num] + dp[num - 1]) % mod
        return dp[2]
```
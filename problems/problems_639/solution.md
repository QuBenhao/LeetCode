# [Python/Java] Dynamic programming

> Author: Benhao
> Date: 2021-09-26
> Upvotes: 15
> Tags: Java, Python, Python3

---

### Approach
Let dp[0] be the `number of ways ending at the previous character`, and dp[1] the `number of ways ending at the current character`.

We have: nxt_dp[0] = dp[1]
Compute nxt_dp[1] as `ways ending at the previous character * ways to decode the current character alone` + `ways ending two characters earlier * ways to decode the previous and current characters together`.

At initialization, the previous prefix is empty and has one decoding. Calculate the number of ways to decode the current character.

Note: Combinations absent from the dictionary are invalid and have zero decodings.

### Code

```Python3 []
ONE = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '*': 9}
TWO = {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '20': 1,
        '21': 1, '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '*0': 2, '*1': 2, '*2': 2, '*3': 2, '*4': 2,
        '*5': 2, '*6': 2, '*7': 1, '*8': 1, '*9': 1, '1*': 9, '2*': 6, '**': 15}
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = 1, ONE.get(s[:1], 0)
        for i in range(1, len(s)):
            dp = dp[1], (ONE.get(s[i], 0) * dp[1] + TWO.get(s[i - 1: i + 1], 0) * dp[0]) % 1000000007
        return dp[-1]
```
```Java []
class Solution {
    int MOD = (int)1e9 + 7;
    static HashMap<String, Integer> one = new HashMap<>(){}, two = new HashMap<>();
    static{
        for(int i=1;i<10;i++)
            one.put(String.format("%d", i), 1);
        one.put("*", 9);
        for(int i=10;i<27;i++)
            two.put(String.format("%d", i), 1);
        for(int i=0;i<7;i++)
            two.put("*"+i, 2);
        for(int i=7;i<10;i++)
            two.put("*"+i, 1);
        two.put("1*", 9);
        two.put("2*", 6);
        two.put("**", 15);
    }
    public int numDecodings(String s) {
        int dp0 = 1, dp1 = one.getOrDefault(s.substring(0,1),0);
        for(int i=1,tmp=0;i<s.length();i++){
            tmp = dp0;
            dp0 = dp1;
            dp1 = (int)(((long)dp1 * one.getOrDefault(s.substring(i,i+1),0) % MOD + (long)tmp * two.getOrDefault(s.substring(i-1,i+1), 0) % MOD) % MOD);
        }
        return dp1;
    }
}
```

```python3
ONE = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '*': 9}
TWO = {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '20': 1,
        '21': 1, '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '*0': 2, '*1': 2, '*2': 2, '*3': 2, '*4': 2,
        '*5': 2, '*6': 2, '*7': 1, '*8': 1, '*9': 1, '1*': 9, '2*': 6, '**': 15}
MOD = 10**9 +7
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 1
            return (ONE.get(s[i], 0) * dfs(i + 1) % MOD + (0 if i == n - 1 else TWO.get(s[i:i+2], 0) * dfs(i + 2)) % MOD)% MOD

        n = len(s)
        return dfs(0)
```

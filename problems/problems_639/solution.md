# [Python/Java] 动态规划

> Author: Benhao
> Date: 2021-09-26
> Upvotes: 15
> Tags: Java, Python, Python3

---

### 解题思路
用dp[0]表示以`上个字符作为结尾的方案数`，用dp[1]表示以`当前字符作为结尾的方案数`。

我们有: nxt_dp[0] = dp[1]
而nxt_dp[1]由以`上个字符结尾方案数 * 当前字符单独解码方案数` + `上上个字符结尾方案数 * 上个字符与当前字符组合的方案数`

初始化的时候，上个字符是空的，方案数为1；求解当前字符解码方案数即可。

注：不出现在字典枚举中的组合即为不存在，认为方案数为0。

### 代码

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
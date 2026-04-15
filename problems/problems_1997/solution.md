# [Python/Java/JavaScript/Go] 类似斐波那契数列的动态规划

> Author: Benhao
> Date: 2022-01-28
> Upvotes: 6
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
受烟花大佬[@megurine](/u/megurine/)的邀请，来做做这道题，确实很有意思。
到达下一个房间需要到达当前房间两次。
而到达当前房间x两次需要从nextVisit[x]再到x一次。
也就是:
$f(x + 1) = f(x) + f(x) - f(nextVisit[x])$
而第一次到达后跳转到nextVisit[x]需要一天，第二次到达后跳转到x+1需要一天
故最终递推关系为:
$f(x + 1) = f(x) + f(x) - f(nextVisit[x]) + 2$

### 代码

```Python3 []
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        # 到达第x+1房间需要先到达第x房间两次，第一次到达x后需要额外一天到达nextVisit[x]，从nextVisit[x]到达x可以用他们的差计算，第二次到达x后仍需额外一天到达x+1
        # f(x + 1) = f(x) + f(x) - f(nextVisit[x]) + 2
        dp = [0] * len(nextVisit)
        dp[0] = 1
        for i in range(1, len(nextVisit)):
            dp[i] = (dp[i - 1] * 2 - dp[nextVisit[i-1]] + 2) % (10 ** 9 + 7)
        return (dp[-1] - 1) % (10 ** 9 + 7)
```
```Java []
class Solution {
    private static int MOD = (int)1e9 + 7;
    public int firstDayBeenInAllRooms(int[] nextVisit) {
        int n = nextVisit.length;
        int[] dp = new int[n];
        dp[0] = 1;
        for(int i = 1;i < n; i++)
            dp[i] = (((MOD + dp[i-1] - dp[nextVisit[i-1]]) % MOD + dp[i-1]) % MOD + 2) % MOD;
        return dp[n - 1] == 0 ? MOD - 1 : dp[n - 1] - 1;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nextVisit
 * @return {number}
 */
const MOD = 1e9 + 7
var firstDayBeenInAllRooms = function(nextVisit) {
    const n = nextVisit.length
    const dp = new Array(n).fill(0)
    dp[0] = 1
    for(let i = 1; i < n; i++)
        dp[i] = ((MOD + dp[i-1] - dp[nextVisit[i-1]]) % MOD + dp[i-1] + 2) % MOD
    return dp[n-1] == 0 ? MOD - 1 : dp[n-1] - 1
};
```
```Go []
const mod int = 1e9 + 7
func firstDayBeenInAllRooms(nextVisit []int) int {
    n := len(nextVisit)
    dp := make([]int, n)
    dp[0] = 1
    for i := 1; i < n; i++ {
        dp[i] = ((mod + dp[i - 1] - dp[nextVisit[i - 1]]) % mod + dp[i - 1] + 2) % mod
    }
    return (mod + dp[n - 1] - 1) % mod
}
```
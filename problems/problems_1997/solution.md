# [Python/Java/JavaScript/Go] Fibonacci-like dynamic programming

> Author: Benhao
> Date: 2022-01-28
> Upvotes: 6
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
烟花 [@megurine](/u/megurine/) invited me to try this problem; it is quite interesting.
Reaching the next room requires visiting the current room twice.
The second visit to room x requires traveling from nextVisit[x] back to x.
That is:
$f(x + 1) = f(x) + f(x) - f(nextVisit[x])$
After the first visit, moving to nextVisit[x] takes one day; after the second, moving to x+1 takes another day.
The final recurrence is therefore:
$f(x + 1) = f(x) + f(x) - f(nextVisit[x]) + 2$

### Code

```Python3 []
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        # To reach room x+1, visit x twice: spend one day moving to nextVisit[x], use the difference of their first-visit times to return to x, then spend one more day moving to x+1
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

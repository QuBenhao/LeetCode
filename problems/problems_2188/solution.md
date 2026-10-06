# [Python/Go] Dynamic programming

> slug: pythongo-dong-tai-gui-hua-by-himymben-fpvv
> date: 2022-02-28
> tags: Go, Python, Python3
> question: Minimum Time to Finish the Race (minimum-time-to-finish-the-race)
> url: https://leetcode.cn/problems/minimum-time-to-finish-the-race/solutions/zDmEFD/pythongo-dong-tai-gui-hua-by-himymben-fpvv/

---
### Approach
A tire's lap time grows exponentially, so after enough laps, even changing to a fresh tire of the same type is faster than continuing.
Precompute the minimum time for each number of consecutive laps across all tires, then use these times in dynamic programming to find the minimum total race time.

### Code

```Python3 []
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        mn = [inf] * 18
        mn[0] = 0
        for f, r in tires:
            cur, base = 0, f
            for i in range(1, len(mn)):
                cur += base
                if base > changeTime + f:
                    break
                if mn[i] > cur:
                    mn[i] = cur
                base *= r
        dp = [inf] * (numLaps + 1)
        dp[0] = -changeTime
        for i in range(1, numLaps + 1):
            for j in range(1, min(i + 1, len(mn))):
                dp[i] = min(dp[i], changeTime + mn[j] + dp[i - j])
        return dp[-1]
```
```Go []
const inf int = math.MaxInt32
func minimumFinishTime(tires [][]int, changeTime int, numLaps int) int {
    mn := make([]int, 18)
    for i := 1; i < len(mn); i++ {
        mn[i] = inf
    }
    for _, tire := range tires {
        f, r := tire[0], tire[1]
        for i, cur, base := 1, 0, f; i < len(mn) && base <= changeTime + f; i++ {
            cur += base
            mn[i] = min(mn[i], cur)
            base *= r
        }  
    }
    dp := make([]int, numLaps + 1)
    dp[0] = -changeTime
    for i := 1; i <= numLaps; i++ {
        dp[i] = inf
        for j := 1; j < min(len(mn), i + 1); j++ {
            dp[i] = min(dp[i], changeTime + mn[j] + dp[i - j])
        }
    }
    return dp[numLaps]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

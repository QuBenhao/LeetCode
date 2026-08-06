# [Python/Go] 动态规划

> slug: pythongo-dong-tai-gui-hua-by-himymben-fpvv
> date: 2022-02-28
> tags: Go, Python, Python3
> question: Minimum Time to Finish the Race (minimum-time-to-finish-the-race)
> url: https://leetcode.cn/problems/minimum-time-to-finish-the-race/solutions/zDmEFD/pythongo-dong-tai-gui-hua-by-himymben-fpvv/

---
### 解题思路
轮胎跑圈的时间是指数增长的，也就是到达一定圈数时，更换成自己重新跑都会比继续跑更优。
预处理统计各个轮胎连续跑一定圈数的最小时间后，用最小时间去统计总共跑圈的最小时间（动态规划）。

### 代码

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
# [Python/Java/Go] 区间dp

> slug: pythonjavago-qu-jian-dp-by-himymben-dswz
> date: 2022-02-03
> tags: Go, Java, Python, Python3
> question: Allocate Mailboxes (allocate-mailboxes)
> url: https://leetcode.cn/problems/allocate-mailboxes/solutions/BQCIHt/pythonjavago-qu-jian-dp-by-himymben-dswz/

---
### 解题思路
预处理各个房屋区间放一个邮箱的距离最小和。
当前从0到i的房屋安排，由【0到i之间选择一个j分割区间后，j到i的房屋里放一个邮箱，与上次0到j的距离和的和】的最小值决定。

### 代码

```Python3 []
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        cost = [[0] * n for _ in range(n)]
        presum = [0] + list(accumulate(houses))
        for i in range(n):
            for j in range(i, n):
                l = j - i + 1
                point = i + l//2
                cost[i][j] = presum[j + 1] - presum[point] * 2 + presum[i] - (houses[point] if l % 2 else 0)
        
        dp = list(cost[0])
        for _ in range(k - 1):
            for i in range(n-1, -1, -1):
                for j in range(i):
                    dp[i] = min(dp[i], dp[j] + cost[j+1][i])
        return dp[-1]
```
```Java []
class Solution {
    public int minDistance(int[] houses, int k) {
        Arrays.sort(houses);
        int n = houses.length;
        int[] presum = new int[n + 1];
        for(int i = 0; i < n; i++)
            presum[i + 1] = presum[i] + houses[i];
        int[][] cost = new int[n][n];
        for(int i = 0; i < n; i++) {
            for(int j = i; j < n; j++) {
                int len = j - i + 1;
                int point = i + len / 2;
                cost[i][j] = presum[j + 1] - presum[point] * 2 + presum[i];
                if(len % 2 == 1)
                    cost[i][j] -= houses[point];
            }
        }
        int[] dp = new int[n];
        for(int i = 0; i < n; i++)
            dp[i] = cost[0][i];
        for(int m = 0; m < k - 1; m++)
            for(int i = n - 1; i >= 0; i--)
                for(int j = 0; j < i; j++)
                    dp[i] = Math.min(dp[i], dp[j] + cost[j+1][i]);
        return dp[n - 1];
    }
}
```
```Go []
func minDistance(houses []int, k int) int {
    sort.Ints(houses)
    n := len(houses)
    presum := make([]int, n + 1)
    for i := 0; i < n; i++ {
        presum[i + 1] = presum[i] + houses[i];
    }
    cost := make([][]int, n)
    for i := 0; i < n; i++ {
        cost[i] = make([]int, n)
        for j := i; j < n; j++ {
            l := j - i + 1
            point := i + l / 2
            cost[i][j] = presum[j + 1] - presum[point] * 2 + presum[i]
            if l & 1 > 0 {
                cost[i][j] -= houses[point]
            }
        }
    }
    dp := make([]int, n)
    copy(dp, cost[0])
    for m := 0; m < k - 1; m++ {
        for r := n - 1; r >= 0; r-- {
            for l := 0; l < r; l++ {
                if v:= dp[l] + cost[l + 1][r]; v < dp[r]{
                    dp[r] = v
                }
            }
        }
    }
    return dp[n - 1]
}
```
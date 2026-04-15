# [Python/Java] 记忆化递归 or 一维dp

> Author: Benhao
> Date: 2021-08-23
> Upvotes: 25
> Tags: Java, Python, Python3

---

### 解题思路
我们从起点出发，能经过最多`k`个城市，相当于我们能离开城市`k+1`次。如果我们到达了终点，返回0；如果我们不是终点也不能再动了，返回inf；返回我们能移动到的所有城市的最小值。

动态规划中，我们可以从src出发(消耗为0)，同样移动k+1次，返回到终点最小的花费。

### 代码

```Python3 []
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        connect = defaultdict(dict)
        for a, b, c in flights:
            connect[a][b] = c

        @lru_cache(None)
        def dfs(city, remain):
            if city == dst:
                return 0
            if not remain:
                return inf
            remain -= 1
            ans = inf
            for nxt in connect[city]:
                ans = min(ans, dfs(nxt, remain) + connect[city][nxt])
            return ans
        
        res = dfs(src, k + 1)
        return res if res != inf else -1
```
```Java []
class Solution {
    int INF = 0x3f3f3f3f;
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[] dp = new int[n];
        Arrays.fill(dp, INF);
        //起点消耗为0
        dp[src] = 0;
        for(int r=0;r<=k;r++){
            // 复制当前走的次数的状态
            int[] nxt = Arrays.copyOf(dp, n);
            // 再移动一次后的状态(到达每个点的花费)
            for(int[] flight:flights){
                int a = flight[0], b = flight[1], c = flight[2];
                nxt[b] = Math.min(nxt[b], dp[a] + c);
            }
            dp = nxt;
        }
        if(dp[dst]<INF)
            return dp[dst];
        return -1;
    }
}
```
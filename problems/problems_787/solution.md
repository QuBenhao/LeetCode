# [Python/Java] Memoized recursion or one-dimensional DP

> Author: Benhao
> Date: 2021-08-23
> Upvotes: 25
> Tags: Java, Python, Python3

---

### Approach
Starting from the source, we can pass through at most `k` intermediate cities, which means leaving a city `k+1` times. Return 0 upon reaching the destination; return inf if we are elsewhere and have no moves left. Otherwise, return the minimum cost over all cities we can move to.

In dynamic programming, start at src with cost 0, allow k+1 moves, and return the minimum cost to the destination.

### Code

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
        // The starting cost is 0
        dp[src] = 0;
        for(int r=0;r<=k;r++){
            // Copy the state for the current number of moves
            int[] nxt = Arrays.copyOf(dp, n);
            // State after one more move: the cost of reaching each node
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

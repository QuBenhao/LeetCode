# [Python] Bitmasking + dynamic programming (memoized recursion, Py 48ms)

> Author: Benhao
> Date: 2021-08-15
> Upvotes: 10
> Tags: Java, Python, Python3

---

### Approach
As with backtracking, place a valid available number at each step. Add 1 only when a complete beautiful arrangement has been formed.
Memoized recursion avoids recalculating a state with the same position and remaining numbers. The position need not be stored separately because it can be inferred from the length of available.

Updated with an improved bitmask approach that recurses in order of the number of choices.

### Code

```Python3 []
class Solution:
    def countArrangement(self, n: int) -> int:
        canFill = defaultdict(list)
        for i in range(1,n+1):
            for j in range(1, n+1):
                # Numbers that can be placed at each position
                if j % i == 0 or i % j == 0:
                    canFill[i].append(j-1)
        # Sort by the number of choices and fill the positions with fewer choices first
        order = sorted(canFill.keys(), key=lambda x:len(canFill[x]))
        end = (1 << n) - 1

        @lru_cache(None)
        def dfs(state):
            # All positions are filled
            if state == end:
                return 1
            cnts = ans = 0
            # The position to fill next
            for i in range(n):
                if (1 << i) & state:
                    cnts += 1
            # Numbers allowed at the current position
            for i in canFill[order[cnts]]:
                # Numbers not yet used
                if not ((1 << i) & state):
                    ans += dfs(state ^ (1 << i))
            return ans
        
        return dfs(0)
```
```Java []
class Solution {
    boolean[][] canFill;
    int[] dp, index;
    boolean[] explored;
    int end;
    int n;
    public int countArrangement(int n_) {
        n = n_;
        canFill = new boolean[n][n];
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                if((j % i == 0) || (i % j == 0))
                    canFill[i-1][j-1] = true;
        PriorityQueue<int[]> queue = new PriorityQueue<>((a,b)->a[1]-b[1]);
        for(int i=0;i<n;i++){
            int cnts = 0;
            for(int j=0;j<n;j++)
                if(canFill[i][j])
                    cnts++;
            queue.add(new int[]{i,cnts});
        }
        index = new int[n];
        int idx=0;
        while(queue.size()!=0){
            index[idx++] = queue.poll()[0];
        }
        end = (1 << n) - 1;
        dp = new int[1<<n];
        explored = new boolean[1<<n];
        return dfs(0);
    }

    public int dfs(int state){
        if(state == end)
            return 1;
        if(explored[state])
            return dp[state];
        explored[state] = true;
        int cnts = 0;
        for(int i=0;i<n;i++)
            if (((1<<i)&state) != 0)
                cnts++;
        for(int i=0;i<n;i++)
            if(canFill[index[cnts]][i] && (((1<<i)&state) == 0)){
                dp[state] += dfs(state | (1 << i));
            }
        return dp[state];
    }
}

```

# [Python] 状态压缩 + 动态规划 (记忆化递归Py 48ms)

> Author: Benhao
> Date: 2021-08-15
> Upvotes: 10
> Tags: Java, Python, Python3

---

### 解题思路
和回溯差不多，每次填入一个合理的可选的数，直到最终填出优美的排列，才累加1。
采用记忆化递归，这样遇到相同位置剩余可选的数相同的情况时，不需要再计算。(注意可以不记录到达第几个数，因为从available的长度即可推)

更新了最佳状态压缩，按可填入个数递归。

### 代码

```Python3 []
class Solution:
    def countArrangement(self, n: int) -> int:
        canFill = defaultdict(list)
        for i in range(1,n+1):
            for j in range(1, n+1):
                # 每个位置可以填入哪些数
                if j % i == 0 or i % j == 0:
                    canFill[i].append(j-1)
        # 根据可填入数字的个数排序，优先填入个数少的
        order = sorted(canFill.keys(), key=lambda x:len(canFill[x]))
        end = (1 << n) - 1

        @lru_cache(None)
        def dfs(state):
            # 全部填入
            if state == end:
                return 1
            cnts = ans = 0
            # 当前该填第几个位置
            for i in range(n):
                if (1 << i) & state:
                    cnts += 1
            # 当前位置可以填哪些数
            for i in canFill[order[cnts]]:
                # 哪些数还没被填
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
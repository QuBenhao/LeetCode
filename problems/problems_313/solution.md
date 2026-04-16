# [Python/Java] 最小堆 o(nmlognm) -> 动态规划o(nm) -> 堆+动态规划 o(nlogm)

> Author: Benhao
> Date: 2021-08-09
> Upvotes: 25
> Tags: Java, Python, Python3

---

### 解题思路

> 最小堆：没有很好地利用给定的primes是递增的这一条件，很暴力地利用最小堆找第n个。【已超时】

丑数的生成方法:已有的丑数乘上某个质因数，构成一个新的丑数，初始丑数仅有1。

> 动态规划： 记录前面的丑数，根据每个质因数当前对应的丑数进行乘积大小对比，将最小的那个作为新的丑数，并更新对应的丑数。

比如[2,3,5]中，一开始所有质因数都对应丑数1，最小的那个是1*2(在1*2,1*3和1*5中最小)，所以我们将**2加入丑数，并更新质因数2对应的丑数为2(不再是1)**，下一次我们对比的就是`2*2,1*3和1*5`了，以此类推，直到我们找到了n个丑数

### 代码
【暴力最小堆已超时】
```Python3 []
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pq = [1]
        seen = {1}
        for i in range(n-1):
            cur = heapq.heappop(pq)
            for p in primes:
                if cur * p not in seen:
                    seen.add(cur * p)
                    heapq.heappush(pq, cur * p)
        return pq[0]
```
```Java []
class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(1);
        Set<Integer> seen = new HashSet<>();
        for(int i=1;i<n;i++){
            int cur = pq.poll();
            for(int p: primes){
                // 防止爆int处理
                if(p > Integer.MAX_VALUE / cur)
                    break;
                if(!seen.contains(cur * p)){
                    seen.add(cur * p);
                    pq.add(cur * p);
                }
            }
        }
        return pq.poll();
    }
}
```

动态规划
```Python3 []
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        # dp[i] 代表第i+1个丑数
        dp = [inf] * n
        dp[0] = 1
        # indexes代表每个质因子现在应该跟哪个丑数相乘
        indexes = [0] * m

        for i in range(1, n):
            # 哪个质因子相乘的丑数将会变化
            changeIndex = 0
            for j in range(m):
                # 如果当前质因子乘它的丑数小于当前的丑数，更新当前丑数并更新变化坐标
                if primes[j] * dp[indexes[j]] < dp[i]:
                    changeIndex = j
                    dp[i] = primes[j] * dp[indexes[j]]
                # 如果相等直接变化，这样可以去重复
                elif primes[j] * dp[indexes[j]] == dp[i]:
                    indexes[j] += 1
            # 变化的坐标+1
            indexes[changeIndex] += 1
        return dp[-1]
```
```Java []
class Solution {
    int m;
    int[] dp, indexes;
    public int nthSuperUglyNumber(int n, int[] primes) {
        m = primes.length;
        dp = new int[n];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 1;
        indexes = new int[m];

        for(int i=1;i<n;i++){
            int minIndex = 0;
            for(int j=0;j<m;j++){
                if(dp[indexes[j]] > Integer.MAX_VALUE / primes[j])
                    continue;
                if(primes[j] * dp[indexes[j]] < dp[i]){
                    dp[i] = primes[j] * dp[indexes[j]];
                    minIndex = j;
                }else if(primes[j] * dp[indexes[j]] == dp[i])
                    indexes[j]++;
            }
            indexes[minIndex]++;
        }
        return dp[n-1];
    }
}
```

堆+动态规划
```Python3 []
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        # dp[i] 代表第i+1个丑数
        dp = [1] * n
        # 丑数, 刚刚乘过的丑数的坐标, 质因数
        pq = [(p, 0, i) for i,p in enumerate(primes)]

        for i in range(1, n):
            # 目前最新的最小的丑数
            dp[i] = pq[0][0]
            # 所有等于这个值的要全部出队列，并根据该乘的丑数重新加入队列
            while pq and pq[0][0] == dp[i]:
                _, idx, p = heapq.heappop(pq)
                heapq.heappush(pq, (dp[idx+1] * primes[p], idx + 1, p))
        return dp[-1]
```
```Java []
// 和三叶同款思路了，照着三叶改了改自己的Java
class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        int m = primes.length;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[0]-b[0]);
        for(int i=0;i<m;i++)
            pq.add(new int[]{primes[i], 0, i});
        int[] dp = new int[n];
        dp[0] = 1;
        
        for(int i=1;i<n;){
            int[] tmp = pq.poll();
            // 丑数，下一个该乘的丑数，质因数
            int val = tmp[0], idx = tmp[1] + 1, p = tmp[2];
            if(val!=dp[i-1]) dp[i++] = val;
            pq.add(new int[]{dp[idx] * primes[p], idx, p});
        }
        return dp[n-1];
    }
}
```
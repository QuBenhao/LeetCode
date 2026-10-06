# [Python/Java] Min-heap o(nmlognm) -> dynamic programming o(nm) -> heap + dynamic programming o(nlogm)

> Author: Benhao
> Date: 2021-08-09
> Upvotes: 25
> Tags: Java, Python, Python3

---

### Approach

> Min-heap: This brute-force approach finds the nth value using a min-heap without making good use of the fact that primes is increasing. [Now times out]

Generate an ugly number by multiplying an existing ugly number by a prime factor. The initial ugly number is 1.

> Dynamic programming: Record previous ugly numbers. For each prime factor, multiply it by its current ugly number, choose the smallest product as the next ugly number, and advance the corresponding index.

For [2,3,5], all prime factors initially point to ugly number 1. The smallest product is 1*2 among 1*2,1*3,1*5, so **add 2 to the ugly numbers and update the ugly number associated with prime factor 2 to 2 instead of 1**. Next compare `2*2,1*3,1*5`, and continue until n ugly numbers have been found.

### Code
[The brute-force min-heap approach now times out]
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
                // Prevent int overflow
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

Dynamic programming
```Python3 []
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        # dp[i] is the (i+1)th ugly number
        dp = [inf] * n
        dp[0] = 1
        # indexes records which ugly number each prime factor should multiply next
        indexes = [0] * m

        for i in range(1, n):
            # Track which prime factor's ugly-number index will change
            changeIndex = 0
            for j in range(m):
                # If a prime factor's product is smaller than the current candidate, update the candidate and the changed index
                if primes[j] * dp[indexes[j]] < dp[i]:
                    changeIndex = j
                    dp[i] = primes[j] * dp[indexes[j]]
                # Advance on equality as well to eliminate duplicates
                elif primes[j] * dp[indexes[j]] == dp[i]:
                    indexes[j] += 1
            # Increment the changed indices
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

Heap + dynamic programming
```Python3 []
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        # dp[i] is the (i+1)th ugly number
        dp = [1] * n
        # Ugly number, index of the ugly number just multiplied, prime factor
        pq = [(p, 0, i) for i,p in enumerate(primes)]

        for i in range(1, n):
            # Current smallest new ugly number
            dp[i] = pq[0][0]
            # Pop every entry equal to this value, then reinsert using the next ugly number to multiply
            while pq and pq[0][0] == dp[i]:
                _, idx, p = heapq.heappop(pq)
                heapq.heappush(pq, (dp[idx+1] * primes[p], idx + 1, p))
        return dp[-1]
```
```Java []
// The same idea as 三叶; I adapted my Java solution accordingly
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
            // Ugly number, next ugly number to multiply, prime factor
            int val = tmp[0], idx = tmp[1] + 1, p = tmp[2];
            if(val!=dp[i-1]) dp[i++] = val;
            pq.add(new int[]{dp[idx] * primes[p], idx, p});
        }
        return dp[n-1];
    }
}
```

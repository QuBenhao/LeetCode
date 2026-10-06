# [Python] Dynamic programming & memoized search: from 2000ms to 32ms

> Author: Benhao
> Date: 2021-07-06
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
Drop an egg from floor $x$; it may break or survive. If it breaks, the answer lies below $x$; otherwise, the answer lies above $x$.
The former case becomes solving $x-1$ floors with $k-1$ eggs; the latter becomes solving $n-x$ floors with $k$ eggs.
We must handle every possibility, so take the larger of the two results. Dropping from this floor therefore costs the maximum of `dp[k-1][x-1], dp[k][n-x]`, plus 1 for this drop.

But we do not know which floor $x$ gives the best solution for $k,n$.
The initial idea is to try every floor and take the minimum result.
That is, `dp[k][n] = min(max(dp[k-1][x-1], dp[k][n-x]) for x in range(1, n)) + 1`.

Scanning n each time to find the maximum times out.
Can this be optimized?

With the same number of eggs, more floors require more operations. As x increases, the left expression increases while the right expression decreases.
Think of the left expression as an increasing curve and the right expression as a decreasing curve; the final answer must be near their intersection.
This monotonicity suggests binary search to find the best $x$ faster.
If the k-1,x-1 side is larger, try a smaller x; if the k,n-x side is larger, try a larger x.
This gives the first implementation (2000ms).

<br>
The submission was still a little slow, so I started thinking about how others made their algorithms so fast.
I considered the problem from another angle.
We still drop eggs, and each may break or survive. But focus on the number of attempts: with $k$ eggs and at most $m$ attempts, how many floors can we test?
If the egg breaks, $k-1$ eggs and $m-1$ attempts remain. If it survives, $k$ eggs remain, but still only $m-1$ attempts. Add the floor from which we dropped the egg.
That is, `dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1`.
Find the smallest m such that dp[k][m] >= n.
This gives the second implementation (700ms).

<br>
Performance still seems insufficient because we may calculate the same k and m many times.
Memoized search eliminates repeated subproblems, giving the third implementation (32ms).

### Code

```python3
class Solution:
    @lru_cache(None)
    def superEggDrop(self, k: int, n: int) -> int:
        if k == 1 or n <= 2:
            return n
        # If k exceeds n, we can use one egg per floor; binary search is the fastest approach
        if k >= n:
            return int(log(n, 2)) + 1
        # Suppose the first drop is from floor x: if the egg breaks, solve x-1 floors with k-1 eggs; otherwise, solve n-x floors with k eggs
        # As x increases, the left side increases and the right decreases; as x decreases, the left decreases and the right increases
        ans = n
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            l = self.superEggDrop(k-1,mid-1)
            r = self.superEggDrop(k, n-mid)
            ans = min(ans, max(l, r) + 1)
            if l >= r:
                right = mid
            else:
                left = mid + 1
        return ans
```

```python3
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # Reverse the question: with k eggs and m attempts, how many floors can we test?
        # Drop an egg; it may break or survive.
        # If it survives, we can handle dp[k][m-1] floors; if it breaks, dp[k-1][m-1] floors; add the floor of this drop.
        # Thus: dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1.
        # The problem becomes finding the smallest m such that dp[k][m] >= n
        dp = [[0] * (n + 1) for _ in range(k+1)]
        dp[1][1] = 1
        for i in range(1, k+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1] + 1
                if i == k and dp[i][j] >= n:
                    return j
        return n
```

```python3
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # Reverse the question: with k eggs and m attempts, how many floors can we test?
        # Drop an egg; it may break or survive.
        # If it survives, we can handle dp[k][m-1] floors; if it breaks, dp[k-1][m-1] floors; add the floor of this drop.
        # Thus: dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1.
        # The problem becomes finding the smallest m such that dp[k][m] >= n
        for i in range(1, n+1):
            if self.maximumFloors(k, i) >= n:
                return i
        return n
    
    @lru_cache(None)
    def maximumFloors(self, k, m):
        if k == 0:
            return 0
        if m == 1:
            return 1
        return self.maximumFloors(k, m-1) + self.maximumFloors(k-1,m-1) + 1
```

# [Python/Java] Memoized recursion (2D DP)

> Author: Benhao
> Date: 2021-08-07
> Upvotes: 13
> Tags: Java, Python, Python3

---

### Approach
With k resizing operations, split the array into k+1 intervals. Each interval must use its maximum value because the size cannot change within that interval.
For each interval, summing (interval maximum - each value) is equivalent to interval maximum * interval length - interval sum.
Every value is subtracted once overall, so the recursion only needs to minimize the sum of interval maximum * interval length.

### Code

```Python3 []
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(idx, left):
            if idx == n:
                return 0
            if not left:
                m = max(nums[idx:])
                return m * (n - idx)
            m = 0
            ans = inf
            for i in range(idx, n - left):
                m = max(m, nums[i])
                ans = min(ans, dfs(i+1, left - 1) + m * (i+1 - idx))
            return ans
        return dfs(0, k) - sum(nums)
```
```Java []
class Solution {
    int INF = 0x3f3f3f3f;
    int n, sum;
    int[][] premax;
    public int minSpaceWastedKResizing(int[] nums, int k) {
        n = nums.length;
        sum = 0;
        int[][] premax = new int[n][n];
        for (int i = 0; i < n; i++){
            int m = 0;
            for(int j = i; j < n; j++){
                m = Math.max(m, nums[j]);
                premax[i][j] = m * (j + 1 - i);
            }
            sum += nums[i];
        }

        int[][] dp = new int[n][k+2];
        for (int i = 0; i < n; i++) Arrays.fill(dp[i], INF);
           
        for (int i = 0; i < n; i++)
            for (int j = 1; j <= k + 1; j++)
                for (int l = 0; l <= i; l++)
                    dp[i][j] = Math.min(dp[i][j], (l == 0 ? 0 : dp[l-1][j-1]) + premax[l][i]); 
        return dp[n-1][k+1] - sum;
    }
}
```

# [Python/Java] 记忆化递归(二维dp)

> Author: Benhao
> Date: 2021-08-07
> Upvotes: 13
> Tags: Java, Python, Python3

---

### 解题思路
我们可以变换k次，也就是我们可以将原数组分成k+1个区间，每个区间必须取区间最大值（认定每个区间内，不能变化，所以必须取区间最大）
原题里每个区间都要求和（区间最大值-每个值），其实拆开算，就是区间最大值*区间长度再减去区间和，
我们最终其实总要减去所有的数，故只要在递归的时候统计我们最小能取到的最大值的各区间和即可。

### 代码

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
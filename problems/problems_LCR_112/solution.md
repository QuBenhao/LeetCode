# [Python/Java] Memoized DFS or memoized dynamic programming?

> slug: python-ji-yi-hua-dfs-by-qubenhao-vb9r
> date: 2021-08-06
> tags: Java, Python, Python3
> question: 矩阵中的最长递增路径 (fpTFWP)
> url: https://leetcode.cn/problems/fpTFWP/solutions/TxQng5/python-ji-yi-hua-dfs-by-qubenhao-vb9r/

---
### Approach
Each cell can move only to a higher-valued neighbor. Memoization records the longest path from each cell, so a new cell reaching a cached cell can reuse that length; the path still satisfies the increasing constraint.

### Code

```Python3 []
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(x, y):
            cur = 0
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[x][y] < matrix[nx][ny]:
                    cur = max(cur, dfs(nx, ny))
            return cur + 1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans
```
```Java []
class Solution {
    int m, n;
    int[][] dp, matrix_;
    int[][] dirs = new int[][]{{-1,0}, {1,0}, {0,1}, {0,-1}};
    public int longestIncreasingPath(int[][] matrix) {
        matrix_ = matrix;
        m = matrix.length;
        n = matrix[0].length;
        dp = new int[m][n];
        int ans = 0;
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                if(dp[i][j]==0)
                    ans = Math.max(ans, dfs(i, j));
        return ans;
    }

    public int dfs(int x, int y){
        if(dp[x][y] != 0)
            return dp[x][y];
        for(int i=0;i<dirs.length;i++){
            int nx = x + dirs[i][0], ny = y + dirs[i][1];
            if(nx >= 0 && nx < m && ny >=0 && ny < n && matrix_[nx][ny] > matrix_[x][y])
                dp[x][y] = Math.max(dp[x][y], dfs(nx, ny));
        }
        return ++dp[x][y];
    }
}
```

# [Python/Java] 记忆化dfs or 记忆化动态规划？

> slug: python-ji-yi-hua-dfs-by-qubenhao-vb9r
> date: 2021-08-06
> tags: Java, Python, Python3
> question: 矩阵中的最长递增路径 (fpTFWP)
> url: https://leetcode.cn/problems/fpTFWP/solutions/TxQng5/python-ji-yi-hua-dfs-by-qubenhao-vb9r/

---
### 解题思路
每个点只能往数值更高的那一侧移动，加入记忆化相当于记录了每个点最长的路径长度，这样新的点如果要走到这个点，直接叠加即可（必然还满足递增性质）

### 代码

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
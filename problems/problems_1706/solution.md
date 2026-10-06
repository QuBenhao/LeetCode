# [Python/Java/JavaScript/Go] Simulation (dynamic programming)

> Author: Benhao
> Date: 2022-02-23
> Upvotes: 16
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Maintain a mapping from each starting column to its column in the current row, and simulate the board in that column.

For a right-sloping board, the ball gets stuck at the last column or when the board on the right slopes left; remove it. Otherwise, move it one column right.
Likewise, for a left-sloping board, the ball gets stuck at the first column or when the board on the left slopes right. Otherwise, move it one column left.

After the last row, the remaining mappings give the balls that exit and their final columns. Return -1 for the stuck balls.

### Code

```Python3 []
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        dp = {i:i for i in range(n)}
        for i in range(m):
            for k in list(dp.keys()):
                if grid[i][dp[k]] == 1:
                    if dp[k] == n - 1 or grid[i][dp[k] + 1] == -1:
                        dp.pop(k)
                    else:
                        dp[k] += 1
                else:
                    if not dp[k] or grid[i][dp[k] - 1] == 1:
                        dp.pop(k)
                    else:
                        dp[k] -= 1
        return [dp[i] if i in dp else -1 for i in range(n)] 
```
```Java []
class Solution {
    public int[] findBall(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] dp = new int[n];
        for(int i = 0; i < n; i++)
            dp[i] = i;
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(dp[j] != - 1) {
                    if(grid[i][dp[j]] == 1) {
                        if(dp[j] == n - 1 || grid[i][dp[j] + 1] == -1)
                            dp[j] = -1;
                        else
                            dp[j]++;
                    } else {
                        if(dp[j] == 0 || grid[i][dp[j] - 1] == 1)
                            dp[j] = -1;
                        else
                            dp[j]--;
                    }
                }
        return dp;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findBall = function(grid) {
    const m = grid.length, n = grid[0].length, dp = new Array(n)
    for(let j = 0; j < n; j++)
        dp[j] = j
    for(let i = 0; i < m; i++)
        for(let j = 0; j < n; j++)
            if(dp[j] != -1) {
                if(grid[i][dp[j]] == 1) {
                    if(dp[j] == n - 1 || grid[i][dp[j] + 1] == -1)
                        dp[j] = -1
                    else
                        dp[j] += 1
                } else {
                    if(dp[j] == 0 || grid[i][dp[j] - 1] == 1)
                        dp[j] = -1
                    else
                        dp[j] -= 1
                }
            }
    return dp
};
```
```Go []
func findBall(grid [][]int) []int {
    m, n, dp := len(grid), len(grid[0]), make([]int, len(grid[0]))
    for i := 0; i < n; i++ {
        dp[i] = i
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if dp[j] != -1 {
                if grid[i][dp[j]] == 1 {
                    if dp[j] == n - 1 || grid[i][dp[j] + 1] == -1 {
                        dp[j] = -1
                    } else {
                        dp[j]++
                    }
                } else {
                    if dp[j] == 0 || grid[i][dp[j] - 1] == 1 {
                        dp[j] = -1
                    } else {
                        dp[j]--
                    }
                }
            }
        }
    }
    return dp
}
```

Concise recursive implementation
```python3
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            return c if r == m else (-1 if (v:=grid[r][c]) and ((not c and v == -1) or (c == n - 1 and v == 1) or v * grid[r][c + v] == -1) else dfs(r + 1, c + v))
        
        return [dfs(0, i) for i in range(n)]
```

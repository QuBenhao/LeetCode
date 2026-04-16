# [Python/Java/JavaScript/Go] 模拟(动态规划)

> Author: Benhao
> Date: 2022-02-23
> Upvotes: 16
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
维护一个出发层纵坐标到当前行纵坐标的映射，根据每行该列的挡板进行模拟。

如果挡板向右，如果坐标是最后一列或者右边的挡板向左，该球会被卡住，删掉；否则它会移动到右边一列。
同理，挡板向左，如果坐标是第一列或者左边的挡板向右，该球会被卡住，删掉；否则它会移动到左边一列。

模拟到最后一行后，还存在的映射为可到达的球及其最终列。其他为卡住的球返回-1。

### 代码

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

简洁递归写法
```python3
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            return c if r == m else (-1 if (v:=grid[r][c]) and ((not c and v == -1) or (c == n - 1 and v == 1) or v * grid[r][c + v] == -1) else dfs(r + 1, c + v))
        
        return [dfs(0, i) for i in range(n)]
```
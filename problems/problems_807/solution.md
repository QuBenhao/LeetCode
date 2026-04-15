# [Python/Java/JavaScript/Go] 求每行每列的最大值

> Author: Benhao
> Date: 2021-12-12
> Upvotes: 23
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
根据题意，每个位置最高的高度取决于原来该行、该列的最大值中的最小值。

### 代码

```Python3 []
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowsMax, colsMax = [max(g) for g in grid], [max(z) for z in zip(*grid)]
        return sum(min(rowsMax[i], colsMax[j]) - grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])))
```
```Java []
class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int[] rowsMax = new int[grid.length], colsMax = new int[grid[0].length];
        for(int i=0;i<grid.length;i++){
            int m = 0;
            for(int j=0;j<grid[0].length;j++)
                m = Math.max(m, grid[i][j]);
            rowsMax[i] = m;
        }
        for(int i=0;i<grid[0].length;i++){
            int m = 0;
            for(int j=0;j<grid.length;j++)
                m = Math.max(m, grid[j][i]);
            colsMax[i] = m;
        }
        int ans = 0;
        for(int i=0;i<grid.length;i++)
            for(int j=0;j<grid[0].length;j++)
                ans += Math.min(rowsMax[i], colsMax[j]) - grid[i][j];
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxIncreaseKeepingSkyline = function(grid) {
    const rowsMax = new Array(grid.length), colsMax = new Array(grid[0].length)
    for(let i=0;i<grid.length;i++){
        let m = 0;
        for(let j=0;j<grid[0].length;j++)
            m = Math.max(m, grid[i][j])
        rowsMax[i] = m
    }
    for(let i=0;i<grid[0].length;i++){
        let m = 0;
        for(let j=0;j<grid.length;j++)
            m = Math.max(m, grid[j][i])
        colsMax[i] = m
    }
    let ans = 0
    for(let i=0;i<grid.length;i++)
        for(let j=0;j<grid[0].length;j++)
            ans += Math.min(rowsMax[i], colsMax[j]) - grid[i][j]
    return ans
};
```
```Go []
func maxIncreaseKeepingSkyline(grid [][]int) int {
    rowsMax, colsMax := make([]int, len(grid)), make([]int, len(grid[0]))
    for i, row := range grid {
        m := 0
        for _, v := range row {
            if v > m {
                m = v
            }
        }
        rowsMax[i] = m
    }
    for i := 0; i < len(grid[0]); i++ {
        m := 0
        for j := 0; j < len(grid); j++ {
            if grid[j][i] > m {
                m = grid[j][i]
            }
        }
        colsMax[i] = m
    }
    ans := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[0]); j++ {
            if rowsMax[i] > colsMax[j] {
                ans += colsMax[j] - grid[i][j]
            } else {
                ans += rowsMax[i] - grid[i][j]
            }
        }
    }
    return ans
}
```

### 复杂度
时间复杂度 $o(m * n)$
空间复杂度 $o(m + n)$
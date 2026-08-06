# [Python/Java/JavaScript/Go] 回溯

> slug: pythonjavajavascriptgo-hui-su-by-himymbe-iczz
> date: 2022-02-05
> tags: Go, Java, JavaScript, Python, Python3
> question: Path with Maximum Gold (path-with-maximum-gold)
> url: https://leetcode.cn/problems/path-with-maximum-gold/solutions/NmpBcc/pythonjavajavascriptgo-hui-su-by-himymbe-iczz/

---
### 解题思路
尝试每一个挖矿起点、回溯每一个路径，返回最大的一个

### 代码

```Python3 []
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0 
        
        def dfs(x, y):
            if x < 0 or y < 0 or x == m or y == n or not grid[x][y]:
                return 0
            record = grid[x][y]
            grid[x][y] = mx = 0
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                mx = max(mx, dfs(x + dx, y + dy))
            grid[x][y] = record
            return record + mx
                
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        
        return ans
```
```Java []
class Solution {
    private static final int[][] DIRS = new int[][]{{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    private int[][] grid;
    private int m, n;
    public int getMaximumGold(int[][] grid_) {
        grid = grid_;
        m = grid.length;
        n = grid[0].length;
        int ans = 0;
        for(int i = 0; i < m; i++) 
            for(int j = 0; j < n; j++)
                ans = Math.max(ans, dfs(i, j));
        return ans;
    }

    private int dfs(int x, int y){
        if(x < 0 || y < 0 || x == m || y == n || grid[x][y] == 0)
            return 0;
        int cur = grid[x][y], max = 0;
        grid[x][y] = 0;
        for(int[] dir: DIRS)
            max = Math.max(max, dfs(x + dir[0], y + dir[1]));
        grid[x][y] = cur;
        return cur + max;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} grid
 * @return {number}
 */
const DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
var getMaximumGold = function(grid) {
    const m = grid.length, n = grid[0].length
    let ans = 0

    dfs = function(x, y) {
        if(x < 0 || y < 0 || x == m || y == n || grid[x][y] == 0)
            return 0
        const cur = grid[x][y]
        let mx = 0
        grid[x][y] = 0
        for(const dir of DIRS)
            mx = Math.max(mx, dfs(x + dir[0], y + dir[1]))
        grid[x][y] = cur
        return cur + mx
    }

    for(let i = 0; i < m; i++)
        for(let j = 0; j < n; j++)
            ans = Math.max(ans, dfs(i, j))
    return ans
};
```
```Go []
func getMaximumGold(grid [][]int) (ans int) {
    m, n := len(grid), len(grid[0])
    var dfs func(x, y int) int
    dfs = func(x, y int) int {
        if x < 0 || y < 0 || x == m || y == n || grid[x][y] == 0 {
            return 0
        }
        cur, mx := grid[x][y], 0
        grid[x][y] = 0
        for _, d := range [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} {
            if v := dfs(x + d[0], y + d[1]); v > mx {
                mx = v
            }
        }
        grid[x][y] = cur
        return cur + mx
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if v := dfs(i, j); v > ans {
                ans = v
            }
        }
    }
    return
}
```

优化：只有角落的矿值得作为起点尝试，非角落的点一般在角落的点的某种路径上，很多是无意义的重复计算。
```python3
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            if x < 0 or y < 0 or x == m or y == n or not grid[x][y]:
                return 0
            record = grid[x][y]
            grid[x][y] = 0
            mx = max(dfs(x + dx, y + dy) for dx, dy in DIRS)
            grid[x][y] = record
            return record + mx
        
        def helper(x, y):
            return sum((nx:=x+dx) < 0 or (ny:=y+dy) < 0 or nx == m or ny == n or not grid[nx][ny] for dx, dy in DIRS) >= 2
        
        return max(dfs(i, j) if grid[i][j] and helper(i, j) else 0 for i in range(m) for j in range(n))
```
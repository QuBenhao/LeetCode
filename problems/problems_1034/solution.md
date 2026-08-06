# [Python/Java/JavaScript/Go] DFS + 记录走过点 or 三色标记法

> slug: pythonjavajavascriptgo-dfs-ji-lu-zou-guo-l7e5
> date: 2021-12-06
> tags: Go, Java, JavaScript, Python, Python3
> question: Coloring A Border (coloring-a-border)
> url: https://leetcode.cn/problems/coloring-a-border/solutions/tIudjn/pythonjavajavascriptgo-dfs-ji-lu-zou-guo-l7e5/

---
### 解题思路
从row，col出发，要通过周围四个点，是否存在非连通分量才进行染色（或者边缘）。那么就需要先标记为访问过，等递归完四周才知道当前点的最终染色结果。

### 代码

记录走过的点
```python3 []
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        explored = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n:
                return True
            if (r,c) in explored:
                return False
            if grid[r][c] != grid[row][col]:
                return True
            explored.add((r,c))
            ans = False
            for dx,dy in (0,1),(1,0),(0,-1),(-1,0):
                if dfs(r+dx,c+dy):
                    ans = True
            if ans:
                grid[r][c] = color
            return False
        
        dfs(row, col)
        return grid
```
```Java []
class Solution {
    private static final int[][] DIRS = new int[][]{{-1,0},{0,1},{1,0},{0,-1}};
    private int[][] grid;
    private Set<Integer> explored;
    private int m,n,row,col,color;
    public int[][] colorBorder(int[][] grid, int row, int col, int color) {
        this.grid = grid;
        explored = new HashSet<>();
        m = this.grid.length;
        n = this.grid[0].length;
        this.row = row;
        this.col = col;
        this.color = color;
        dfs(row, col);
        return this.grid;
    }

    private boolean dfs(int r, int c) {
        if(r < 0 || c < 0 || r == m || c == n)
            return true;
        int p = r * n + c;
        if(explored.contains(p))
            return false;
        if(grid[r][c] != grid[row][col])
            return true;
        explored.add(p);
        boolean cur = false;
        for(int[] dir: DIRS)
            if(dfs(r+dir[0],c+dir[1]))
                cur = true;
        if(cur)
            grid[r][c] = color;
        return false;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} grid
 * @param {number} row
 * @param {number} col
 * @param {number} color
 * @return {number[][]}
 */
const DIRS = [[-1, 0], [0, 1], [0, -1], [1, 0]]
var colorBorder = function(grid, row, col, color) {
    const m = grid.length, n = grid[0].length, explored = new Set()
    dfs = function(r, c) {
        if(r < 0 || c < 0 || r == m || c == n)
            return true
        const p = r * n + c
        if(explored.has(p))
            return false
        if(grid[r][c] != grid[row][col])
            return true
        explored.add(p)
        let cur = false
        for(const dir of DIRS)
            if(dfs(r+dir[0],c+dir[1]))
                cur = true
        if(cur)
            grid[r][c] = color
        return false
    }

    dfs(row, col)
    return grid
};
```
```Go []
func colorBorder(grid [][]int, row int, col int, color int) [][]int {
    m, n, explored, dirs := len(grid), len(grid[0]), map[int]bool{}, [][]int{{0,1},{1,0},{-1,0},{0,-1}}

    var dfs func(r,c int) bool 
    dfs = func(r,c int) bool {
        if r < 0 || c < 0 || r == m || c == n {
            return true
        }
        p := r * n + c
        if explored[p] {
            return false
        }
        if grid[r][c] != grid[row][col] {
            return true
        }
        explored[p] = true
        cur := false
        for _, dir := range dirs {
            if dfs(r + dir[0], c + dir[1]) {
                cur = true
            }
        }
        if cur {
            grid[r][c] = color
        }
        return false
    }
    dfs(row, col)
    return grid
}
```

三色标记
```Python3 []
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        b = grid[row][col]

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n:
                return True
            if not grid[r][c] or grid[r][c] == -1:
                return False
            if grid[r][c] != b:
                return True
            grid[r][c], ans = 0, False
            for dx,dy in (0,1),(1,0),(0,-1),(-1,0):
                if dfs(r+dx,c+dy):
                    ans = True
            if ans:
                grid[r][c] = -1
            return False
        
        dfs(row, col)
        for r in range(m):
            for c in range(n):
                if not grid[r][c]:
                    grid[r][c] = b
                elif grid[r][c] == -1:
                    grid[r][c] = color
        return grid
```
```Java []
class Solution {
    private static final int[][] DIRS = new int[][]{{-1,0},{0,1},{1,0},{0,-1}};
    private int[][] grid;
    private int m,n,row,col,b;
    public int[][] colorBorder(int[][] grid, int row, int col, int color) {
        this.grid = grid;
        m = this.grid.length;
        n = this.grid[0].length;
        this.row = row;
        this.col = col;
        b = grid[row][col];
        dfs(row, col);
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                if(this.grid[i][j] == 0)
                    this.grid[i][j] = b;
                else if(this.grid[i][j] == -1)
                    this.grid[i][j] = color;
        return this.grid;
    }

    private boolean dfs(int r, int c) {
        if(r < 0 || c < 0 || r == m || c == n)
            return true;
        if(grid[r][c] == 0 || grid[r][c] == -1)
            return false;
        if(grid[r][c] != b)
            return true;
        grid[r][c] = 0;
        boolean cur = false;
        for(int[] dir: DIRS)
            if(dfs(r+dir[0],c+dir[1]))
                cur = true;
        if(cur)
            grid[r][c] = -1;
        return false;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} grid
 * @param {number} row
 * @param {number} col
 * @param {number} color
 * @return {number[][]}
 */
const DIRS = [[-1, 0], [0, 1], [0, -1], [1, 0]]
var colorBorder = function(grid, row, col, color) {
    const m = grid.length, n = grid[0].length, b = grid[row][col]
    dfs = function(r, c) {
        if(r < 0 || c < 0 || r == m || c == n)
            return true
        if(grid[r][c] == 0 || grid[r][c] == -1)
            return false
        if(grid[r][c] != b)
            return true
        grid[r][c] = 0
        let cur = false
        for(const dir of DIRS)
            if(dfs(r+dir[0],c+dir[1]))
                cur = true
        if(cur)
            grid[r][c] = -1
        return false
    }

    dfs(row, col)
    for(let i=0;i<m;i++)
        for(let j=0;j<n;j++)
            if(grid[i][j] == 0)
                grid[i][j] = b
            else if(grid[i][j] == -1)
                grid[i][j] = color
    return grid
};
```
```Go []
func colorBorder(grid [][]int, row int, col int, color int) [][]int {
    m, n, dirs, b := len(grid), len(grid[0]), [][]int{{0,1},{1,0},{-1,0},{0,-1}}, grid[row][col]

    var dfs func(r,c int) bool 
    dfs = func(r,c int) bool {
        if r < 0 || c < 0 || r == m || c == n {
            return true
        }
        if grid[r][c] == 0 || grid[r][c] == -1 {
            return false
        }
        if grid[r][c] != b {
            return true
        }
        grid[r][c] = 0
        cur := false
        for _, dir := range dirs {
            if dfs(r + dir[0], c + dir[1]) {
                cur = true
            }
        }
        if cur {
            grid[r][c] = -1
        }
        return false
    }
    dfs(row, col)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 0 {
                grid[i][j] = b
            } else if grid[i][j] == -1 {
                grid[i][j] = color
            }
        }
    }
    return grid
}
```

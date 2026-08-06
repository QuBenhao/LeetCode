# [Python/Java/JavaScript/Go] 多源BFS or DFS

> slug: pythonjavajavascriptgo-duo-yuan-bfs-by-h-by6l
> date: 2022-02-12
> tags: Go, Java, JavaScript, Python, Python3
> question: Number of Enclaves (number-of-enclaves)
> url: https://leetcode.cn/problems/number-of-enclaves/solutions/vMKqf2/pythonjavajavascriptgo-duo-yuan-bfs-by-h-by6l/

---
### 解题思路
从四条外边的陆地出发的BFS。默写一下多源BFS即可

### 代码
多源BFS
```Python3 []
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        for i in range(m):
            # 第一列
            if grid[i][0]:
                queue.append((i, 0))
                grid[i][0] = 0
            # 最后一列
            if grid[i][n - 1]:
                queue.append((i, n - 1))
                grid[i][n - 1] = 0
        for j in range(n):
            # 第一行
            if grid[0][j]:
                queue.append((0, j))
                grid[0][j] = 0
            # 最后一行
            if grid[m - 1][j]:
                queue.append((m - 1, j))
                grid[m - 1][j] = 0
        while queue:
            x, y = queue.popleft()
            for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                if 0 <= (nx := x + dx) < m and 0 <= (ny := y + dy) < n and grid[nx][ny]:
                    grid[nx][ny] = 0
                    queue.append((nx, ny))
        return sum(sum(g) for g in grid)
```
```Java []
class Solution {
    private static final int[][] DIRS = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    public int numEnclaves(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Deque<int[]> queue = new ArrayDeque<>();
        for(int i = 0; i < m; i++) {
            if(grid[i][0] == 1) {
                grid[i][0] = 0;
                queue.add(new int[]{i, 0});
            }
            if(grid[i][n - 1] == 1) {
                grid[i][n - 1] = 0;
                queue.add(new int[]{i, n - 1});
            }
        }
        for(int j = 0; j < n; j++) {
            if(grid[0][j] == 1) {
                grid[0][j] = 0;
                queue.add(new int[]{0, j});
            }
            if(grid[m - 1][j] == 1) {
                grid[m - 1][j] = 0;
                queue.add(new int[]{m - 1, j});
            }
        }
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            for(int[] dir: DIRS) {
                int nx = cur[0] + dir[0], ny = cur[1] + dir[1];
                if(nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1) {
                    grid[nx][ny] = 0;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
        int ans = 0;
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(grid[i][j] == 1)
                    ans++;
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} grid
 * @return {number}
 */
const DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
var numEnclaves = function(grid) {
    const queue = new Array(), m = grid.length, n = grid[0].length
    let idx = 0
    for(let i = 0; i < m; i++) {
        if(grid[i][0] == 1) {
            grid[i][0] = 0
            queue.push([i, 0])
        }
        if(grid[i][n - 1] == 1) {
            grid[i][n - 1] = 0
            queue.push([i, n - 1])
        }
    }
    for(let j = 0; j < n; j++) {
        if(grid[0][j] == 1) {
            grid[0][j] = 0
            queue.push([0, j])
        }
        if(grid[m - 1][j] == 1) {
            grid[m - 1][j] = 0
            queue.push([m - 1, j])
        }
    }
    while(idx < queue.length) {
        const cur = queue[idx++]
        for(const dir of DIRS) {
            const nx = cur[0] + dir[0], ny = cur[1] + dir[1]
            if(nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1) {
                grid[nx][ny] = 0
                queue.push([nx, ny])
            }
        }
    }
    let ans = 0
    for(let i = 0; i < m; i++)
        for(let j = 0; j < n; j++)
            if(grid[i][j] == 1)
                ans++
    return ans
};
```
```Go []
func numEnclaves(grid [][]int) (ans int) {
    m, n, queue := len(grid), len(grid[0]), [][]int{}
    for i := 0; i < m; i++ {
        if grid[i][0] == 1 {
            grid[i][0] = 0
            queue = append(queue, []int{i, 0})
        }
        if grid[i][n - 1] == 1 {
            grid[i][n - 1] = 0
            queue = append(queue, []int{i, n - 1})
        }
    }
    for j := 0; j < n; j++ {
        if grid[0][j] == 1 {
            grid[0][j] = 0
            queue = append(queue, []int{0, j})
        }
        if grid[m - 1][j] == 1 {
            grid[m - 1][j] = 0
            queue = append(queue, []int{m - 1, j})
        }
    }
    for len(queue) > 0 {
        cur := queue[0]
        queue = queue[1:]
        for _, dir := range [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} {
            nx, ny := cur[0] + dir[0], cur[1] + dir[1]
            if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1 {
                grid[nx][ny] = 0
                queue = append(queue, []int{nx, ny})
            }
        }
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                ans++
            }
        }
    }
    return
}
```

DFS
```python3
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                if 0 <= (nx := x + dx) < m and 0 <= (ny := y + dy) < n and grid[nx][ny]:
                    grid[nx][ny] = 0
                    dfs(nx, ny)
        for i in range(m):
            if grid[i][0]:
                grid[i][0] = 0
                dfs(i, 0)
            if grid[i][n - 1]:
                grid[i][n - 1] = 0
                dfs(i, n - 1)
        for j in range(n):
            if grid[0][j]:
                grid[0][j] = 0
                dfs(0, j)
            if grid[m - 1][j]:
                grid[m - 1][j] = 0
                dfs(m - 1, j)
        return sum(sum(g) for g in grid)
```
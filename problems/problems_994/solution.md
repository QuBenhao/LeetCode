# [Python/Java/JavaScript/Go] 多源BFS

> Author: Benhao
> Date: 2022-01-28
> Upvotes: 5
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
标准的多源BFS，从多个腐烂的橘子作为初始点开始广度优先搜索，用原始grid标记访问过。

### 代码

```Python3 []
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cost, cnts, queue, m, n = 0, 0, [], len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    cnts += 1
                    if v == 2:
                        queue.append((i, j))
        while queue:
            nxt = []
            cnts -= len(queue)
            for i, j in queue:
                for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                    if 0 <= (nx := i + dx) < m and 0 <= (ny := j + dy) < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        nxt.append((nx, ny))
            queue, cost = nxt, cost + 1 if nxt else cost
        return cost if not cnts else -1
```
```Java []
class Solution {
    private static final int[][] DIRS = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    public int orangesRotting(int[][] grid) {
        int cnts = 0, cost = 0, m = grid.length, n = grid[0].length;
        Deque<Integer> queue = new ArrayDeque<>();
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(grid[i][j] > 0){
                    cnts++;
                    if(grid[i][j] == 2)
                        queue.addLast(i * n + j);
                }
        while(!queue.isEmpty()){
            int len = queue.size();
            cnts -= len;
            for(int i = 0; i < len; i++){
                int point = queue.pollFirst();
                int x = point / n, y = point % n;
                for(int[] d: DIRS){
                    int nx = x + d[0], ny = y + d[1];
                    if(nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1){
                        grid[nx][ny] = 2;
                        queue.addLast(nx * n + ny);
                    }
                }
            }
            if(!queue.isEmpty()){
                cost++;
            }
        }
        return cnts == 0 ? cost : -1;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} grid
 * @return {number}
 */
const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
var orangesRotting = function(grid) {
    const m = grid.length, n = grid[0].length
    let cnts = 0, cost = 0, queue = new Array()
    for(let i = 0; i < m; i++)
        for(let j = 0; j < n; j++)
            if(grid[i][j] > 0){
                cnts++
                if(grid[i][j] == 2)
                    queue.push([i, j])
            }
    while(queue.length > 0){
        const nxt = new Array()
        cnts -= queue.length
        for(const p of queue){
            for(const d of dirs){
                const nx = p[0] + d[0], ny = p[1] + d[1]
                if(nx >= 0 && ny >= 0 && nx < m && ny < n && grid[nx][ny] == 1){
                    grid[nx][ny] = 2
                    nxt.push([nx, ny])
                }
            }
        }
        queue = nxt
        if(queue.length > 0)
            cost++
    }
    return cnts == 0 ? cost : -1
};
```
```Go []
func orangesRotting(grid [][]int) int {
    cnts, cost, m, n, queue := 0, 0, len(grid), len(grid[0]), [][]int{}
    for i, row := range grid{
        for j, v := range row {
            if v > 0 {
                cnts++
                if v == 2{
                    queue = append(queue, []int{i, j})
                }
            }
        }
    }
    for len(queue) > 0{
        l := len(queue)
        cnts -= l
        for i := 0; i < l; i++{
            point := queue[0]
            queue = queue[1:]
            for _, d := range [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}{
                nx, ny := point[0] + d[0], point[1] + d[1]
                if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1{
                    grid[nx][ny] = 2
                    queue = append(queue, []int{nx, ny})
                }
            }
        }
        if len(queue) > 0{
            cost++
        }
    }
    if cnts == 0 {
        return cost
    }
    return -1
}
```
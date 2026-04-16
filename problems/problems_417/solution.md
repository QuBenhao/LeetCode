# [Python/Java/JavaScript/Go] 多源BFS or DFS

> Author: Benhao
> Date: 2022-04-26
> Upvotes: 21
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
从边出发，只要有比自己高的点，就往高处走，直到走不了为止。
最终返回太平洋和大西洋能走到的点的交集。
说明这些点可以流到太平洋和大西洋。

PS:
给出py中二维转一维 和 tuple 的两种写法

### 代码

```Python3 []
DIRS = (0, 1), (0, -1), (-1, 0), (1, 0)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def bfs(queue):
            explored = set(queue)
            while queue:
                cur = queue.popleft()
                x, y = divmod(cur, n)
                for dx, dy in DIRS:
                    if 0 <= (nx := x + dx) < m and 0 <= (ny := y + dy) < n and heights[nx][ny] >= heights[x][y] and (nxt := nx * n + ny) not in explored:
                        queue.append(nxt)
                        explored.add(nxt)
            return explored
        
        pacific = bfs(deque([i for i in range(n)] + [i * n for i in range(1, m)]))
        atlantic = bfs(deque([(m - 1) * n + i for i in range(n)] + [(i + 1) * n - 1 for i in range(m - 1)]))
        return list(list(divmod(p, n)) for p in pacific & atlantic)
```
```Java []
class Solution {
    private static final int[][] DIRS = new int[][]{{1, 0}, {0, 1}, {0, -1}, {-1, 0}};
    private int m, n;
    private int[][] h;
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        m = heights.length;
        n = heights[0].length;
        h = heights;
        Deque<Integer> pacific = new ArrayDeque<>(), atlantic = new ArrayDeque<>();
        int last = (m - 1) * n;
        for(int i = 0; i < n; i++) {
            pacific.addLast(i);
            atlantic.addLast(last + i);
        }
        for(int i = 1; i < m; i++) {
            pacific.addLast(i * n);
            atlantic.addLast((m - i) * n - 1);
        }
        Set<Integer> s1 = bfs(pacific), s2 = bfs(atlantic);
        List<List<Integer>> ans = new ArrayList<>();
        Set<Integer> s;
        if(s2.size() < s1.size()) {
            s2.retainAll(s1);
            s = s2;
        }
        else {
            s1.retainAll(s2);
            s = s1;
        }
        for(int p: s) {
            List<Integer> list = new ArrayList();
            int x = p / n, y = p % n;
            list.add(x);
            list.add(y);
            ans.add(list);
        }
        return ans;
    }

    private Set<Integer> bfs(Deque<Integer> queue) {
        Set<Integer> explored = new HashSet<>(queue);
        while(queue.size() > 0) {
            int cur = queue.pollFirst();
            int x = cur / n, y = cur % n;
            for(int[] dir: DIRS) {
                int nx = x + dir[0], ny = y + dir[1];
                int nxt = nx * n + ny;
                if(0 <= nx && nx < m && 0 <= ny && ny < n && h[nx][ny] >= h[x][y] && !explored.contains(nxt)) {
                    queue.addLast(nxt);
                    explored.add(nxt);
                }
            }
        }
        return explored;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
var pacificAtlantic = function(heights) {
    const m = heights.length, n = heights[0].length
    bfs = function(start) {
        const explored = new Set(start)
        while(start.length > 0) {
            const nxt_arr = new Array()
            for(const p of start) {
                const x = Math.floor(p / n), y = p % n
                for(const dir of dirs) {
                    const nx = x + dir[0], ny = y + dir[1]
                    const nxt = nx * n + ny
                    if(0 <= nx && nx < m && 0 <= ny && ny < n && heights[nx][ny] >= heights[x][y] && !explored.has(nxt)) {
                        explored.add(nxt)
                        nxt_arr.push(nxt)
                    }
                }
            }
            start = nxt_arr
        }
        return explored
    }

    const pacific = new Array(), atlantic = new Array()
    for(let i = 0; i < n; i++) {
        pacific.push(i)
        atlantic.push((m - 1) * n + i)
    }
    for(let i = 1; i < m; i++) {
        pacific.push(i * n)
        atlantic.push((m - i) * n - 1)
    }
    const s1 = bfs(pacific), s2 = bfs(atlantic), ans = new Array()
    for(const p of s1)
        if(s2.has(p))
            ans.push([Math.floor(p / n), p % n])
    return ans
};
```
```Go []
func pacificAtlantic(heights [][]int) (ans [][]int) {
    m, n := len(heights), len(heights[0])
    bfs := func(queue []int) map[int]bool {
        res := map[int]bool{}
        for _, p := range queue {
            res[p] = true
        }
        for len(queue) > 0 {
            cur := queue[0]
            queue = queue[1:]
            x, y := cur / n, cur % n
            for _, dir := range [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} {
                if nx, ny, nxt := x + dir[0], y + dir[1], (x + dir[0]) * n + (y + dir[1]); 0 <= nx && nx < m && 0 <= ny && ny < n && heights[nx][ny] >= heights[x][y] && !res[nxt] {
                    res[nxt] = true
                    queue = append(queue, nxt)
                }
            }
        }
        return res
    }

    pacific, atlantic := []int{}, []int{}
    for i := 0; i < n; i++ {
        pacific = append(pacific, i)
        atlantic = append(atlantic, (m - 1) * n + i)
    }
    for i := 1; i < m; i++ {
        pacific = append(pacific, i * n)
        atlantic = append(atlantic, (m - i) * n - 1)
    }
    m1, m2 := bfs(pacific), bfs(atlantic)
    for k := range m1 {
        if m2[k] {
            ans = append(ans, []int{k / n, k % n})
        }
    }
    return
}
```

dfs
```python3
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def helper(start):
            explored = set(start)
            def dfs(x, y):
                for dx, dy in DIRS:
                    if 0 <= (nx := x + dx) < m and 0 <= (ny := y + dy) < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in explored:
                        explored.add((nx, ny))
                        dfs(nx, ny)
            for sx, sy in start:
                dfs(sx, sy)
            return explored
        
        return list(map(list, helper([(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]) &
                              helper([(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)])))
```
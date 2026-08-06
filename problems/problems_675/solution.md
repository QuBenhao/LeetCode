# [Python/Java/JavaScript/Go] BFS or A*

> slug: pythonjavajavascriptgo-bfs-by-himymben-3hjb
> date: 2022-05-23
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Cut Off Trees for Golf Event (cut-off-trees-for-golf-event)
> url: https://leetcode.cn/problems/cut-off-trees-for-golf-event/solutions/dCMSf2/pythonjavajavascriptgo-bfs-by-himymben-3hjb/

---
### 解题思路
题目其实是多次BFS的意思。每次都求从当前最矮的树到次矮的树的最小距离，最后累加答案即可。
(PS: 根据题目数据范围, 我们需要对输入做排序和映射为坐标的处理)

当然这个方法在本题不是最优解，因为会有很多重复计算在里面(多次计算两点之间的最短距离，可能会有重叠)。

补充一个A star写法，heuristic函数使用曼哈顿距离即可。

### 代码

```Python3 []
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        trees = sorted((forest[i][j], i, j) for i, j in product(range(m), range(n)) if forest[i][j] > 1)

        def bfs(start, end):
            queue = deque([(start, 0)])
            explored = [list(r) for r in forest]
            while queue:
                cur, cost = queue.popleft()
                if cur == end:
                    return cost
                x, y = cur
                cost += 1
                for dx, dy in DIRS:
                    if 0 <= (nx := x + dx) < m and 0 <= (ny := y + dy) < n and explored[nx][ny]:
                        explored[nx][ny] = 0
                        queue.append(((nx, ny), cost))
            return -1
        
        ans = bfs((0, 0), trees[0][1:])
        for a, b in pairwise(trees):
            if (res := bfs(a[1:], b[1:])) == -1:
                return -1
            ans += res
        return ans
```
```Java []
class Solution {
    private static final int[][] DIRS = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    private int m, n;
    private List<List<Integer>> graph;
    public int cutOffTree(List<List<Integer>> forest) {
        m = forest.size();
        n = forest.get(0).size();
        graph = forest;
        List<int[]> trees = new ArrayList<>();
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(forest.get(i).get(j) > 1) {
                    trees.add(new int[]{forest.get(i).get(j), i * n + j});
                }
            }
        }
        Collections.sort(trees, (a, b) -> a[0] - b[0]);
        int ans = bfs(0, trees.get(0)[1]);
        for(int i = 0; i < trees.size() - 1; i++) {
            int res = bfs(trees.get(i)[1], trees.get(i + 1)[1]);
            if(res == -1) {
                return -1;
            }
            ans += res;
        }
        return ans;
    }

    private int bfs(int start, int end) {
        Set<Integer> explored = new HashSet<>(){{add(start);}};
        Deque<int[]> queue = new ArrayDeque<>();
        queue.addLast(new int[]{start, 0});
        while(!queue.isEmpty()) {
            int[] cur = queue.pollFirst();
            int x = cur[0] / n, y = cur[0] % n, cost = cur[1];
            if(cur[0] == end) {
                return cost;
            }
            for(int[] dir: DIRS) {
                int dx = dir[0], dy = dir[1];
                int nx = x + dx, ny = y + dy;
                int p = nx * n + ny;
                if(0 <= nx && nx < m && 0 <= ny && ny < n && graph.get(nx).get(ny) > 0 && !explored.contains(p)) {
                    explored.add(p);
                    queue.addLast(new int[]{p, cost + 1});
                }
            }
        }
        return -1;
    }
}
```
```TypeScript []
const DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
function cutOffTree(forest: number[][]): number {
    const m = forest.length, n = forest[0].length, trees = new Array()
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(forest[i][j] > 1) {
                trees.push([forest[i][j], i, j])
            }
        }
    }
    trees.sort((a, b) => a[0] - b[0])

    const bfs = (x1: number, y1: number, x2: number, y2: number): number => {
        if (x1 == x2 && y1 == y2) {
            return 0
        }
        const explored = new Set()
        let queue = new Array(), cost = 0
        queue.push([x1, y1])
        while(queue.length > 0) {
            let nxt = new Array()
            for(const [x, y] of queue) {
                for(const [dx, dy] of DIRS) {
                    const nx = x + dx, ny = y + dy
                    const p = nx * n + ny
                    if(0 <= nx && nx < m && 0 <= ny && ny < n && forest[nx][ny] > 0 && !explored.has(p)) {
                        if(nx == x2 && ny == y2) {
                            return cost + 1
                        }
                        explored.add(p)
                        nxt.push([nx, ny])
                    }
                }
            }
            queue = nxt
            cost += 1
        }
        return -1
    }

    let ans = bfs(0, 0, trees[0][1], trees[0][2])
    for(let i = 0; i < trees.length - 1; i++) {
        const [, x1, y1] = trees[i], [, x2, y2] = trees[i + 1]
        const res = bfs(x1, y1, x2, y2)
        if (res == -1) {
            return -1
        }
        ans += res
    }
    return ans
};
```
```Go []
func cutOffTree(forest [][]int) int {
    m, n := len(forest), len(forest[0])
    trees := [][]int{}
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if forest[i][j] > 1 {
                trees = append(trees, []int{forest[i][j], i * n + j})
            }
        }
    }
    sort.Slice(trees, func(i, j int) bool { 
        return trees[i][0] < trees[j][0]
    })
    dirs := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

    bfs := func(start, end int) int {
        queue, explored := [][]int{{start, 0}}, map[int]bool{}
        for len(queue) > 0 {
            first := queue[0]
            cur, cost := first[0], first[1]
            if cur == end {
                return cost
            }
            x, y := cur / n, cur % n
            queue = queue[1:]
            for _, d := range dirs {
                nx, ny := x + d[0], y + d[1]
                p := nx * n + ny
                if 0 <= nx && nx < m && 0 <= ny && ny < n && forest[nx][ny] > 0 && !explored[p] {
                    explored[p] = true
                    queue = append(queue, []int{p, cost + 1})
                }
            }
        }
        return -1
    }

    ans := bfs(0, trees[0][1])
    for i := 0; i < len(trees) - 1; i++ {
        if res := bfs(trees[i][1], trees[i + 1][1]); res == -1 {
            return res
        } else {
            ans += res
        }
    }
    return ans
}
```

```python3
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        idx_map = {forest[i][j]: (i, j) for i in range(m) for j in range(n) if forest[i][j] > 1}
        nums = sorted(idx_map.keys())
        explored = defaultdict(lambda: inf)

        def h(p, idx):
            x1, y1 = idx_map[nums[idx]]
            x2, y2 = p
            return abs(x2 - x1) + abs(y2 - y1)

        # f(n) = h(n) + g(n), g(n), idx, point
        pq = [(h((0, 0), 0), 0, 0, (0, 0))]
        explored[(0, 0, 0)] = 0
        mem = set()
        while pq:
            _, cost, idx, point = heappop(pq)
            if idx in mem:
                continue
            x, y = point
            if forest[x][y] == nums[idx]:
                if idx == len(nums) - 1:
                    return cost
                forest[x][y] = 1
                mem.add(idx)
                idx += 1
            cost += 1
            for dx, dy in DIRS:
                if 0 <= (nx := x + dx) < m and 0 <= (ny := y + dy) < n and forest[nx][ny] and explored[(nx, ny, idx)] > cost:
                    explored[(nx, ny, idx)] = cost
                    heappush(pq, (h((nx, ny), idx) + cost, cost, idx, (nx, ny)))
        return -1
```
# [Python/Java/TypeScript/Go] DFS + 标记岛屿 + 枚举变化点

> Author: Benhao
> Date: 2022-09-18
> Upvotes: 13
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
1. 遍历 + DFS 统计已知所有岛屿的面积以及将岛屿标号、将点映射到岛屿的标号上
2. 枚举变化点，统计它四周点所属岛屿及面积，返回最大值即可

### 代码

```Python3 []
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, mp, idx, size_map, res = len(grid), dict(), 0, dict(), 0

        def dfs(x, y):
            ans = 1
            mp[(x, y)] = idx
            for dx, dy in DIRS:
                if 0 <= (nx := x + dx) < n and 0 <= (ny := y + dy) < n and grid[nx][ny] and (nx, ny) not in mp:
                    ans += dfs(nx, ny)
            return ans

        for i in range(n):
            for j in range(n):
                if grid[i][j] and (i, j) not in mp:
                    size_map[idx] = dfs(i, j)
                    res = max(res, size_map[idx])
                    idx += 1

        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    tmp, cur = set(), 1
                    for dx, dy in DIRS:
                        if 0 <= (nx := i + dx) < n and 0 <= (ny := j + dy) < n and grid[nx][ny] and mp[(nx, ny)] not in tmp:
                            tmp.add(mp[(nx, ny)])
                            cur += size_map[mp[(nx, ny)]]
                    res = max(res, cur)
        return res
```
```Java []
class Solution {
    private static final int[][] DIRS = new int[][]{{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
    private Map<Integer, Integer> map, sizeMap;
    private int n, idx, res;
    private int[][] grid;

    public int largestIsland(int[][] g) {
        map = new HashMap<>();
        sizeMap = new HashMap<>();
        n = g.length;
        idx = res = 0;
        grid = g;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    int mark = n * i + j;
                    if (!map.containsKey(mark)) {
                        int size = dfs(i, j);
                        sizeMap.put(idx++, size);
                        res = Math.max(res, size);
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    Set<Integer> tmp = new HashSet<>(4);
                    int cur = 1;
                    for (int[] dir: DIRS) {
                        int nx = i + dir[0], ny = j + dir[1];
                        if (0 <= nx && nx < n && 0 <= ny && ny < n && grid[nx][ny] == 1) {
                            int mark = nx * n + ny;
                            if (!tmp.contains(map.get(mark))) {
                                tmp.add(map.get(mark));
                                cur += sizeMap.get(map.get(mark));
                            }
                        }
                    }
                    res = Math.max(res, cur);
                }
            }
        }
        return res;
    }

    private int dfs(int x, int y) {
        int ans = 1, mark = n * x + y;
        map.put(mark, idx);
        for (int[] dir: DIRS) {
            int nx = x + dir[0], ny = y + dir[1];
            if (0 <= nx && nx < n && 0 <= ny && ny < n && grid[nx][ny] == 1) {
                int nextMark = nx * n + ny;
                if (!map.containsKey(nextMark)) {
                    ans += dfs(nx, ny);
                }
            }
        }
        return ans;
    }
}
```
```TypeScript []
const DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
function largestIsland(grid: number[][]): number {
    const mp: Map<number, number> = new Map<number, number>(), sizeMap: Map<number, number> = new Map<number, number>(), n: number = grid.length
    let idx: number = 0, res: number = 0

    const getMark = (i: number, j: number): number => {
        return i * n + j
    }, dfs = (x: number, y: number): number => {
        let ans: number = 1
        mp.set(getMark(x, y), idx)
        for (const [dx, dy] of DIRS) {
            const nx: number = x + dx, ny: number = y + dy
            if (0 <= nx && nx < n && 0 <= ny && ny < n && grid[nx][ny] == 1 && !mp.has(getMark(nx, ny))) {
                ans += dfs(nx, ny)
            }
        }
        return ans
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] == 1 && !mp.has(getMark(i, j))) {
                const size: number = dfs(i, j)
                sizeMap.set(idx++, size)
                res = Math.max(res, size)
            }
        }
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] == 0) {
                const tmp: Set<number> = new Set<number>()
                let cur: number = 1
                for (const [dx, dy] of DIRS) {
                    const nx: number = i + dx, ny: number = j + dy
                    if (0 <= nx && nx < n && 0 <= ny && ny < n && grid[nx][ny] == 1) {
                        const mark: number = getMark(nx, ny)
                        if (!tmp.has(mp.get(mark))) {
                            tmp.add(mp.get(mark))
                            cur += sizeMap.get(mp.get(mark))
                        }
                    }
                }
                res = Math.max(res, cur)
            }
        }
    }
    return res
};
```
```Go []
func largestIsland(grid [][]int) (res int) {
    n, mp, idx, sizeMap := len(grid), map[int]int{}, 0, map[int]int{}

    getMark := func(i, j int) int {
        return i * n + j
    }

    var dfs func(x, y int) int
    dfs = func(x, y int) int {
        ans := 1
        mp[getMark(x, y)] = idx
        for _, nxt := range [][]int{{x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1}} {
            if 0 <= nxt[0] && nxt[0] < n && 0 <= nxt[1] && nxt[1] < n && grid[nxt[0]][nxt[1]] == 1 {
                if _, ok := mp[getMark(nxt[0], nxt[1])]; !ok {
                    ans += dfs(nxt[0], nxt[1])
                }
            }
        }
        return ans
    }

    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                if _, ok := mp[getMark(i, j)]; !ok {
                    size := dfs(i, j)
                    sizeMap[idx] = size
                    res = max(res, size)
                    idx++
                }
            }
        }
    }

    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 0 {
                tmp, cur := map[int]bool{}, 1
                for _, nxt := range [][]int{{i + 1, j}, {i - 1, j}, {i, j + 1}, {i, j - 1}} {
                    if 0 <= nxt[0] && nxt[0] < n && 0 <= nxt[1] && nxt[1] < n && grid[nxt[0]][nxt[1]] == 1 {
                        if curIdx := mp[getMark(nxt[0], nxt[1])]; !tmp[curIdx] {
                            tmp[curIdx] = true
                            cur += sizeMap[curIdx]
                        }
                    }
                }
                res = max(res, cur)
            }
        }
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

PS: 可以直接修改原数组作为标记，省去空间和坐标转换
```Python3
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, idx, size_map, res = len(grid), 2, dict(), 0

        def dfs(x, y):
            ans = 1
            grid[x][y] = idx
            for dx, dy in DIRS:
                if 0 <= (nx := x + dx) < n and 0 <= (ny := y + dy) < n and grid[nx][ny] == 1:
                    ans += dfs(nx, ny)
            return ans

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size_map[idx] = dfs(i, j)
                    res = max(res, size_map[idx])
                    idx += 1

        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    tmp, cur = {0}, 1
                    for dx, dy in DIRS:
                        if 0 <= (nx := i + dx) < n and 0 <= (ny := j + dy) < n and grid[nx][ny] not in tmp:
                            tmp.add(grid[nx][ny])
                            cur += size_map[grid[nx][ny]]
                    res = max(res, cur)
        return res
```
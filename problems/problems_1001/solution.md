# [Python/Java/JavaScript/Go] 简单模拟

> slug: pythonjavajavascriptgo-jian-dan-mo-ni-by-hd3j
> date: 2022-02-07
> tags: Go, Java, JavaScript, Python, Python3
> question: Grid Illumination (grid-illumination)
> url: https://leetcode.cn/problems/grid-illumination/solutions/ZeyXWU/pythonjavajavascriptgo-jian-dan-mo-ni-by-hd3j/

---
### 解题思路
维护四个计数和点的集合。

四个计数分别为：行计数、列计数、左对角线计数、右对角线计数（国际象棋皇后能威慑到的所有格子）
这样我们只需要知道查询点在任意计数上是否大于0，就知道它是不是被照亮了。
再根据点的集合删除点，删除点的时候同样更新各个计数情况即可

### 代码

```Python3 []
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row_cnts, col_cnts, lr_cnts, rl_cnts, points = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), set()
        for r, c in lamps:
            if (r, c) not in points:
                points.add((r, c))
                row_cnts[r] += 1
                col_cnts[c] += 1
                # r * (-1) + b = c
                lr_cnts[r + c] += 1
                # r + b = c
                rl_cnts[r - c] += 1
        ans = [0] * len(queries)
        for i in range(len(queries)):
            r, c = queries[i]
            if row_cnts[r] or col_cnts[c] or lr_cnts[r + c] or rl_cnts[r - c]:
                ans[i] = 1
                for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0), (0, 0), (1, 1), (-1, 1), (1, -1), (-1, -1):
                    if ((nx := r + dx),(ny := c + dy)) in points:
                        points.remove((nx, ny))
                        row_cnts[nx] -= 1
                        col_cnts[ny] -= 1
                        lr_cnts[nx + ny] -= 1
                        rl_cnts[nx - ny] -= 1
        return ans
```
```Java []
class Solution {
    private static final int[][] DIRS = new int[][]{{0, 0}, {0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
    private Map<Integer, Integer> rowCnts, colCnts, lrCnts, rlCnts;
    public int[] gridIllumination(int n, int[][] lamps, int[][] queries) {
        long ln = (long)n;
        rowCnts = new HashMap<>();
        colCnts = new HashMap<>();
        lrCnts = new HashMap<>();
        rlCnts = new HashMap<>();
        Set<Long> points = new HashSet<>();
        for(int[] lamp: lamps) {
            int x = lamp[0], y = lamp[1];
            long p = ln * x + y;
            if(!points.contains(p)) {
                points.add(p);
                operate(x, y, 1);
            }
        }
        int[] ans = new int[queries.length];
        for(int i = 0; i < queries.length; i++) {
            int x = queries[i][0], y = queries[i][1];
            if(rowCnts.getOrDefault(x, 0) > 0 || colCnts.getOrDefault(y, 0) > 0 || lrCnts.getOrDefault(x + y, 0) > 0 || rlCnts.getOrDefault(x - y, 0) > 0){
                ans[i] = 1;
                for(int[] dir: DIRS){
                    int nx = x + dir[0], ny = y + dir[1];
                    if(nx >= 0 && ny >= 0 && nx < n && ny < n){
                        long p = ln * nx + ny;
                        if(points.contains(p)){
                            points.remove(p);
                            operate(nx, ny, -1);
                        }
                    }
                }
            }
        }
        return ans;
    }

    private void operate(Integer x, Integer y, int diff) {
        add(rowCnts, x, diff);
        add(colCnts, y, diff);
        add(lrCnts, x + y, diff);
        add(rlCnts, x - y, diff);
    }

    private void add(Map<Integer,Integer> map, Integer key, int val) {
        int cur = map.getOrDefault(key, 0);
        map.put(key, cur + val);
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number[][]} lamps
 * @param {number[][]} queries
 * @return {number[]}
 */
const DIRS = [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
var gridIllumination = function(n, lamps, queries) {
    const rowCnts = new Map(), colCnts = new Map(), lrCnts = new Map(), rlCnts = new Map(), points = new Set()

    update = function(map, key, val) {
        if(map.has(key)){
            let v = map.get(key)
            v += val
            if(v == 0)
                map.delete(key)
            else
                map.set(key, v)
        } else {
            map.set(key, val)
        }
    }

    operate = function(x, y, diff) {
        update(rowCnts, x, diff)
        update(colCnts, y, diff)
        update(lrCnts, x + y, diff)
        update(rlCnts, x - y, diff)
    }

    for(const lamp of lamps) {
        const x = lamp[0], y = lamp[1]
        const p = BigInt(x * n + y)
        if(!points.has(p)) {
            points.add(p)
            operate(x, y, 1)
        }
    }

    const ans = new Array(queries.length).fill(0)
    for(let i = 0; i < queries.length; i++) {
        const x = queries[i][0], y = queries[i][1]
        if(rowCnts.has(x) || colCnts.has(y) || lrCnts.has(x + y) || rlCnts.has(x - y)) {
            ans[i] = 1
            for(const dir of DIRS) {
                const nx = x + dir[0], ny = y + dir[1]
                if(nx >= 0 && ny >= 0 && nx < n && ny < n) {
                    const p = BigInt(nx * n + ny)
                    if(points.has(p)) {
                        points.delete(p)
                        operate(nx, ny, -1)
                    }
                }
            }
        }        
    }
    return ans
};
```
```Go []
func gridIllumination(n int, lamps [][]int, queries [][]int) []int {
    rowCnts, colCnts, lrCnts, rlCnts, points := map[int]int{}, map[int]int{}, map[int]int{}, map[int]int{}, map[int]bool{}
    for _, lamp := range lamps {
        x, y := lamp[0], lamp[1]
        p := x * n + y
        if(!points[p]) {
            points[p] = true
            rowCnts[x] += 1
            colCnts[y] += 1
            lrCnts[x + y] += 1
            rlCnts[x - y] += 1
        }
    }

    ans := make([]int, len(queries))
    for i := 0; i < len(queries); i++ {
        x, y := queries[i][0], queries[i][1]
        if(rowCnts[x] > 0 || colCnts[y] > 0 || lrCnts[x + y] > 0 || rlCnts[x - y] > 0) {
            ans[i] = 1
            for _, dir := range [][]int{{0, 0}, {0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}} {
                nx, ny := x + dir[0], y + dir[1]
                if nx >= 0 && ny >= 0 && nx < n && ny < n {
                    p := nx * n + ny
                    if(points[p]) {
                        points[p] = false
                        rowCnts[nx] -= 1
                        colCnts[ny] -= 1
                        lrCnts[nx + ny] -= 1
                        rlCnts[nx - ny] -= 1
                    }
                }
            }
        }
    }
    return ans
}

```
# [Python/Java/JavaScript/Go] 有大小上界的BFS

> slug: pythonjavajavascriptgo-you-da-xiao-shang-j04b
> date: 2022-01-10
> tags: Go, Java, JavaScript, Python, Python3
> question: Escape a Large Maze (escape-a-large-maze)
> url: https://leetcode.cn/problems/escape-a-large-maze/solutions/6m8tQ5/pythonjavajavascriptgo-you-da-xiao-shang-j04b/

---
### 解题思路
因为blocked的大小只有不到200，而棋盘大小相对于200几乎是无限大，遍历光棋盘必然会超时。

blocked有几种能包围中一个区域的方式。
```python
"""
在棋盘角落
   x
  x
 x
x

在其他地方
 x
x x
 x
"""
```
只有利用棋盘边缘的方式可以最大程度上拥有一个限制区域，而我们广度优先搜索时，只要大小超过该区域，棋子必然不足以封锁住我们的路线了。
角落的最大区域大小为$\frac{n * (n-1)}{2}$,其中$n$为blocked的长度。

### 代码

```Python3 []
BOUND = int(1e6)
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked, MAX = {tuple(p) for p in blocked}, len(blocked) * (len(blocked) - 1) // 2

        def bfs(start, end):
            points,idx,explored = [start], 0, {tuple(start)}
            while idx < len(points):
                for dx, dy in (0, 1), (1,0),(-1,0),(0, -1):
                    nx, ny = points[idx][0] + dx, points[idx][1] + dy
                    if 0 <= nx < BOUND and 0 <= ny < BOUND and (nx, ny) not in blocked and (nx, ny) not in explored:
                        if [nx, ny] == end:
                            return True
                        explored.add((nx, ny))
                        points.append((nx, ny))
                if len(points) > MAX:
                    return True
                idx += 1
            return False
        
        return bfs(source, target) and bfs(target, source)
```
```Java []
class Solution {
    private static final int BOUND = (int)1e6;
    private static final long HASH_BOUND = (long)1e6;
    private static final int[][] dir = new int[][]{{1,0},{0,1},{0,-1},{-1,0}};
    private Set<Long> block;

    public boolean isEscapePossible(int[][] blocked, int[] source, int[] target) {
        int max = blocked.length * (blocked.length - 1) / 2;
        block = new HashSet<>();
        for(int[] p: blocked)
            block.add(p[0] * HASH_BOUND + p[1]);
        return bfs(source, target, max) && bfs(target, source, max);
    }

    private boolean bfs(int[] start, int[] end, int max){
        List<int[]> list = new ArrayList<>(){{add(start);}};
        Set<Long> explored = new HashSet<>(){{add(start[0] * HASH_BOUND + start[1]);}};
        for(int i=0;i<list.size() && list.size() <= max;i++)
            for(int j=0;j<dir.length;j++){
                int[] point = new int[]{list.get(i)[0] + dir[j][0], list.get(i)[1] + dir[j][1]};
                long p = point[0] * HASH_BOUND + point[1];
                if(point[0] >= 0 && point[0] < BOUND && point[1] >= 0 && point[1] < BOUND && !explored.contains(p) && !block.contains(p)){
                    if(point[0] == end[0] && point[1] == end[1])
                        return true;
                    explored.add(p);
                    list.add(point);
                }
            }
        return list.size() > max;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} blocked
 * @param {number[]} source
 * @param {number[]} target
 * @return {boolean}
 */
const BOUND = 1000000
const DIR = [[0, 1], [1, 0], [-1,0],[0,-1]]
var isEscapePossible = function(blocked, source, target) {
    const max = Math.floor(blocked.length * (blocked.length - 1) / 2);
    block = new Set()
    for(const b of blocked)
        block.add(b[0] * BOUND + b[1])
    bfs = function(start, end){
        const list = [start], explored = new Set()
        explored.add(start[0] * BOUND + start[1])
        for(let i=0;i<list.length && list.length <= max; i++)
            for(const dir of DIR){
                const point = [list[i][0] + dir[0], list[i][1] + dir[1]]
                const hash = point[0] * BOUND + point[1]
                if(point[0] >= 0 && point[0] < BOUND && point[1] >= 0 && point[1] < BOUND && !block.has(hash) && !explored.has(hash)){
                    if(point[0] == end[0] && point[1] == end[1])
                        return true
                    explored.add(hash)
                    list.push(point)
                }
            }
        return list.length > max
    }
    return bfs(source, target) && bfs(target, source)
};
```
```Go []
func isEscapePossible(blocked [][]int, source []int, target []int) bool {
    bound, block, max, dir := 1000000, map[int]bool{}, len(blocked) * (len(blocked) - 1) / 2, [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
    for _, b := range blocked{
        block[hash(b)] = true
    }
    bfs := func(start, end []int)bool {
        list := [][]int{start}
        explored := map[int]bool{}
        explored[hash(start)] = true
        for i := 0; i < len(list) && len(list) <= max; i++{
            for _, d := range dir {
                point := make([]int, 2)
                point[0] = list[i][0] + d[0]
                point[1] = list[i][1] + d[1]
                h := hash(point)
                if point[0] >= 0 && point[0] < bound && point[1] >= 0 && point[1] < bound && !explored[h] && !block[h]{
                    if point[0] == end[0] && point[1] == end[1]{
                        return true
                    }
                    explored[h] = true
                    list = append(list, point)
                }
            }
        }
        return len(list) > max
    }

    return bfs(source, target) && bfs(target, source)
}

func hash(point []int) int {
    return point[0] * 1000000 + point[1]
}
```
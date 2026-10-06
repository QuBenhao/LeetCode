# [Python/Java/JavaScript/Go] Minimax game

> Author: Benhao
> Date: 2022-01-03
> Upvotes: 55
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
For the mouse, winning is best, with a score of -1; a draw is next, with a score of 0; the worst outcome is a cat win, with a score of 1.
The mouse therefore wants the smallest possible score, while the cat wants the largest. This is a classic minimax game.

Draw analysis: after enough moves to explore every state that could lead to a win, the game still has not ended.
**It takes $2 * n^2$ states to exhaust all possibilities before an identical state repeats; $2*n$ is insufficient to identify a draw**

Thanks to [@AC_Mikoto](/u/ac_mikoto/) for the test cases.
> [[5, 7, 9], [3, 4, 5, 6], [3, 4, 5, 8], [1, 2, 6, 7], [1, 2, 5, 7, 9], [0, 1, 2, 4, 8], [1, 3, 7, 8], [0, 3, 4, 6, 8], [2, 5, 6, 7, 9], [0, 4, 8]]
> [[2, 4, 6], [2, 5, 6, 7], [0, 1, 6, 8, 9], [4, 5, 7, 9], [0, 3, 6, 7, 8], [1, 3, 6, 7, 9], [0, 1, 2, 4, 5, 9], [1, 3, 4, 5, 8], [2, 4, 7, 9], [2, 3, 5, 6, 8]]
> [[7], [2, 6, 8, 9], [1, 4, 5, 6, 7], [4, 5, 7], [2, 3, 5, 8], [2, 3, 4, 7], [1, 2, 9], [0, 2, 3, 5, 9], [1, 4, 9], [1, 6, 7, 8]]

### Code

Pasting a solution here; I have not finished reading it yet
```python3
class Solution(object):
    def catMouseGame(self, graph):
        N = len(graph)

        # What nodes could play their turn to
        # arrive at node (m, c, t) ?
        def parents(m, c, t):
            if t == 2:
                for m2 in graph[m]:
                    yield m2, c, 3-t
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 3-t

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)

        # degree[node] : the number of neutral children of this node
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[m,c,1] = len(graph[m])
                degree[m,c,2] = len(graph[c]) - (0 in graph[c])

        # enqueued : all nodes that are colored
        queue = collections.deque([])
        for i in range(N):
            for t in range(1, 3):
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))

        # percolate
        while queue:
            # for nodes that are colored :
            i, j, t, c = queue.popleft()
            # for every parent of this node i, j, t :
            for i2, j2, t2 in parents(i, j, t):
                # if this parent is not colored :
                if color[i2, j2, t2] is DRAW:
                    # if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if t2 == c: # winning move
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    # else, this parent has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[i2, j2, t2] -= 1
                        if degree[i2, j2, t2] == 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))

        return color[1, 2, 1]
```

```python3 []
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(m, c, i):
            """
            Minimax game:
            The mouse seeks a win first, then accepts a draw
            The cat seeks a win first, then accepts a draw

            :param m: The mouse's position
            :param c: The cat's position
            :param i: The turn
            """
            if i > 100:
                return 0
            if not m:
                return -1
            if c == m:
                return 1
            res = (-1) ** i
            if i % 2:
                for nxt in graph[c]:
                    if nxt:
                        res = max(res, dfs(m, nxt, i + 1))
                    if res == 1:
                        break
            else:
                for nxt in graph[m]:
                    res = min(res, dfs(nxt, c, i + 1))
                    if res == -1:
                        break
            return res
        return ans if not (ans:=dfs(1, 2, 0)) else (1 if ans == -1 else 2)
```
```Java []
class Solution {
    private Map<Integer, Map<Integer, Integer>> cache;
    private int[][] graph;
    public int catMouseGame(int[][] graph_) {
        cache = new HashMap<>();
        graph = graph_;
        int ans = minMax(0, 1, 2);
        if(ans == -1)
            return 1;
        else if(ans == 1)
            return 2;
        return 0;
    }

    private int minMax(int i, int m, int c){
        if(i > 2 * graph.length)
            return 0;
        if(m == 0)
            return -1;
        if(c == m)
            return 1;
        Map<Integer, Integer> memo = cache.getOrDefault(i, new HashMap<Integer, Integer>());
        int key = m * graph.length + c;
        if(memo.containsKey(key))
            return memo.get(key);
        int res = i % 2 == 0 ? 1 : -1;
        if(i % 2 == 0){
            for(int nxt: graph[m]){
                res = Math.min(res, minMax(i + 1, nxt, c));
                if(res == -1)
                    break;
            }
        }else{
            for(int nxt: graph[c]){
                if(nxt != 0){
                    res = Math.max(res, minMax(i + 1, m, nxt));
                    if(res == 1)
                        break;
                }
            }
        }
        memo.put(key, res);
        cache.put(i, memo);
        return res;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} graph
 * @return {number}
 */
var catMouseGame = function(graph) {
    const n = graph.length
    const memo = new Array(n * 2).fill(0).map(() => new Array(n).fill(0).map(() => new Array(n).fill(-2)));
    minMax = function(i, m, c){
        if(i == n * 2)
            return 0
        if(m == 0)
            return -1
        if(c == m)
            return 1
        if(memo[i][m][c] != -2)
            return memo[i][m][c]
        let res = i % 2 == 0? 1 : -1
        if(i % 2 == 0){
            for(const nxt of graph[m]){
                res = Math.min(res, minMax(i + 1, nxt, c))
                if(res == -1)
                    break
            }
        }else{
            for(const nxt of graph[c]){
                if(nxt != 0){
                    res = Math.max(res, minMax(i + 1, m, nxt))
                    if(res == 1)
                        break
                }
            }
        }
        memo[i][m][c] = res
        return res
    }
    const ans = minMax(0, 1, 2)
    if(ans == -1)
        return 1
    if(ans == 1)
        return 2
    return 0
};
```
```Go []
func catMouseGame(graph [][]int) int {
    n := len(graph)
    memo := make([][][]int, 2 * n)
    for i := 0; i < 2 * n; i++{
        memo[i] = make([][]int, n)
        for j := 0; j < n; j++{
            memo[i][j] = make([]int, n)
            for k := range memo[i][j] {
                memo[i][j][k] = -2
            }
        }
    }

    var minMax func(i, m, c int) int
    minMax = func(i, m, c int) int {
        if i == 2 * n {
            return 0
        }
        if m == 0 {
            return -1
        }
        if c == m {
            return 1
        }
        if memo[i][m][c] != -2{
            return memo[i][m][c]
        }
        var res int
        if i % 2 == 1 {
            res = -1
            for _, nxt := range graph[c]{
                if nxt != 0 {
                    r := minMax(i+1,m,nxt)
                    if r > res{
                        res = r
                    }
                    if r == 1 {
                        break
                    }
                }
            }
        }else{
            res = 1
            for _, nxt := range graph[m]{
                r := minMax(i+1,nxt,c)
                if r < res{
                    res = r
                }
                if r == -1 {
                    break
                }
            }
        }
        memo[i][m][c] = res
        return res
    }

    ans := minMax(0, 1, 2)
    if ans == -1 {
        return 1
    }else if ans == 1 {
        return 2
    }
    return 0
}
```

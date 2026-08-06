# [Python/Java/JavaScript/Go] BFS记录次短距离

> slug: pythonjavajavascriptgo-bfsji-lu-ci-duan-671ei
> date: 2022-01-23
> tags: Go, Java, JavaScript, Python, Python3
> question: Second Minimum Time to Reach Destination (second-minimum-time-to-reach-destination)
> url: https://leetcode.cn/problems/second-minimum-time-to-reach-destination/solutions/pbySa5/pythonjavajavascriptgo-bfsji-lu-ci-duan-671ei/

---
### 解题思路
由于time和change是固定的，而不是在不同边有不同的值，所以我们可以统计出起点到终点的最短距离和次短距离，然后根据次短距离计算答案。

### 代码

```python3 []
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        # idx, dist
        pq = deque([(1, 0)])
        explored = [[inf] * 2 for _ in range(n)]
        explored[0][0] = 0
        while pq:
            idx, dist = pq.popleft()
            for other in graph[idx]:
                if dist + 1 < explored[other - 1][0]:
                    explored[other - 1][0] = dist + 1
                elif explored[other - 1][0] < dist + 1 < explored[other - 1][1]:
                    explored[other - 1][1] = dist + 1
                    if other == n:
                        ans = 0
                        for i in range(explored[-1][1]):
                            ans += time
                            if i < explored[-1][1] - 1 and (ans // change) % 2:
                                ans = (ans + change) // change * change
                        return ans
                else:
                    continue
                pq.append((other, dist + 1))
        return -1
```
```Java []
class Solution {
    private static final int INF = 0x3f3f3f3f;
    public int secondMinimum(int n, int[][] edges, int time, int change) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for(int[] edge: edges){
            List<Integer> a = graph.getOrDefault(edge[0] - 1, new ArrayList<>());
            List<Integer> b = graph.getOrDefault(edge[1] - 1, new ArrayList<>());
            a.add(edge[1] - 1);
            b.add(edge[0] - 1);
            graph.put(edge[0] - 1, a);
            graph.put(edge[1] - 1, b);
        }
        int[][] explored = new int[n][2];
        for(int i=0;i<n;i++)
            Arrays.fill(explored[i], INF);
        Deque<int[]> queue = new ArrayDeque<>();
        queue.addLast(new int[]{0, 0});
        explored[0][0] = 0;
        out:
        while(!queue.isEmpty()){
            int[] cur = queue.pollFirst();
            int idx = cur[0], nxtDist = cur[1] + 1;
            for(int other: graph.get(idx)){
                if(nxtDist < explored[other][0])
                    explored[other][0] = nxtDist;
                else if(nxtDist > explored[other][0] && nxtDist < explored[other][1]){
                    explored[other][1] = nxtDist;
                    if(other == n - 1)
                        break out;
                }
                else
                    continue;
                queue.addLast(new int[]{other, nxtDist});
            }
        }
        int ans = 0;
        for(int i=0;i<explored[n-1][1];i++){
            ans += time;
            if(i < explored[n-1][1] - 1 && (ans / change) % 2 == 1)
                ans = (ans + change) / change * change; 
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} time
 * @param {number} change
 * @return {number}
 */
const INF = 0x3f3f3f3f
var secondMinimum = function(n, edges, time, change) {
    const graph = new Array(n).fill(0).map(() => new Array());
    for (const edge of edges) {
        graph[edge[0] - 1].push(edge[1] - 1);
        graph[edge[1] - 1].push(edge[0] - 1);
    }
    const explored = new Array(n).fill(0).map(() => new Array(2).fill(INF))
    let queue = [0], dist = 0
    out:
    while(queue.length > 0){
        dist += 1
        const nxt = new Array()
        for(const idx of queue)
            for(const other of graph[idx]){
                if(explored[other][0] > dist)
                    explored[other][0] = dist
                else if(explored[other][0] < dist && explored[other][1] > dist){
                    explored[other][1] = dist
                    if(other == n - 1)
                        break out
                }
                else
                    continue
                nxt.push(other)
            }
        queue = nxt
    }
    let ans = 0
    for(let i = 0; i < explored[n-1][1]; i++){
        ans += time
        if(i < explored[n-1][1] -1 && Math.floor(ans/change) % 2 == 1)
            ans = Math.floor((ans + change)/change) * change
    }
    return ans
};
```
```Go []
const inf int = 0x3f3f3f3f
func secondMinimum(n int, edges [][]int, time int, change int) (ans int) {
    graph := map[int][]int{}
    for _, edge := range edges{
        graph[edge[0] - 1] = append(graph[edge[0] - 1], edge[1] - 1)
        graph[edge[1] - 1] = append(graph[edge[1] - 1], edge[0] - 1)
    }
    explored := make([][]int, n)
    for i := 0; i < n; i++{
        explored[i] = []int{inf, inf}
    }
    explored[0][0] = 0
    queue := [][]int{{0, 0}}
    out:
    for len(queue) > 0{
        idx, dist := queue[0][0], queue[0][1]
        queue = queue[1:]
        for _, other := range graph[idx]{
            if explored[other][0] > dist + 1{
                explored[other][0] = dist + 1
            } else if explored[other][0] < dist + 1 && explored[other][1] > dist + 1{
                explored[other][1] = dist + 1
                if other == n - 1{
                    break out
                }
            } else{
                continue
            }
            queue = append(queue, []int{other, dist + 1})
        }
    }
    for i := 0; i < explored[n - 1][1]; i++ {
        ans += time
        if i < explored[n-1][1] - 1 && (ans / change) % 2 == 1{
            ans = (ans + change)/change * change
        }
    }
    return
}
```
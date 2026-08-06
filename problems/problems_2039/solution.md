# [Python/Java/JavaScript/Go] BFS

> slug: -by-himymben-tu1u
> date: 2022-03-20
> tags: Go, Java, JavaScript, Python, Python3
> question: The Time When the Network Becomes Idle (the-time-when-the-network-becomes-idle)
> url: https://leetcode.cn/problems/the-time-when-the-network-becomes-idle/solutions/rZ2l0a/-by-himymben-tu1u/

---
### 解题思路
用BFS统计每个服务器$i$到0服务器的最短距离$d_i$，那么该服务器第一次接收到服务器的消息的时间为$d_i * 2$，
于是该服务器最后一次发出消息的时间为$\lfloor \frac{d_i * 2 - 1}{p} \rfloor * p$ (这里的减一是因为收到消息的那一刻不会再发消息)，
该服务器最后一次消息回复的时间为$\lfloor \frac{d_i * 2 - 1}{p} \rfloor * p + d_i * 2$

### 代码

```Python3 []
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        distance = [inf] * n
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        queue = deque([(0, 0)])
        distance[0] = 0
        while queue:
            server, cost = queue.popleft()
            distance[server] = cost
            for other in graph[server]:
                if distance[other] == inf:
                    distance[other] = cost + 1
                    queue.append((other, cost + 1))
        ans = 0
        for i in range(n):
            d, p = distance[i] * 2, patience[i]
            ans = max(ans, (d - 1) // p * p + d if p else 0)
        return ans + 1
```
```Java []
class Solution {
    public int networkBecomesIdle(int[][] edges, int[] patience) {
        int n = patience.length;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for(int[] edge : edges) {
            List<Integer> l1 = graph.getOrDefault(edge[0], new ArrayList<>()), l2 = graph.getOrDefault(edge[1], new ArrayList<>());
            l1.add(edge[1]);
            l2.add(edge[0]);
            graph.put(edge[0], l1);
            graph.put(edge[1], l2);
        }
        int[] distance = new int[n];
        distance[0] = -1;
        Deque<int[]> deque = new ArrayDeque<>();
        deque.addLast(new int[]{0, 0});
        while(!deque.isEmpty()) {
            int[] cur = deque.pollFirst();
            for(int other: graph.get(cur[0])) {
                if(distance[other] == 0) {
                    distance[other] = cur[1] + 1;
                    deque.addLast(new int[]{other, cur[1] + 1});
                }
            }
        }
        int ans = 0;
        for(int i = 1; i < n; i++) {
            int d = distance[i] * 2, p = patience[i];
            ans = Math.max(ans, (d - 1) / p * p + d);
        }
        return ans + 1;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} edges
 * @param {number[]} patience
 * @return {number}
 */
var networkBecomesIdle = function(edges, patience) {
    const n = patience.length, graph = new Map()
    for(const edge of edges) {
        var l1, l2
        if(graph.has(edge[0]))
            l1 = graph.get(edge[0])
        else
            l1 = new Array()
        l1.push(edge[1])
        graph.set(edge[0], l1)
        if(graph.has(edge[1]))
            l2 = graph.get(edge[1])
        else
            l2 = new Array()
        l2.push(edge[0])
        graph.set(edge[1], l2)
    }
    const distance = new Array(n).fill(Number.MAX_SAFE_INTEGER)
    distance[0] = 0
    let queue = [0], cost = 0
    while(queue.length > 0) {
        cost += 1
        next = new Array()
        for(const server of queue)
            for(const other of graph.get(server))
                if(distance[other] == Number.MAX_SAFE_INTEGER) {
                    distance[other] = cost
                    next.push(other)
                }
        queue = next
    }
    let ans = 0
    for(let i = 1; i < n; i++) {
        const d = distance[i] * 2, p = patience[i]
        ans = Math.max(ans, Math.floor((d - 1) / p) * p + d)
    }
    return ans + 1
};
```
```Go []
func networkBecomesIdle(edges [][]int, patience []int) (ans int) {
    n, graph := len(patience), map[int][]int{}
    for _, edge := range edges {
        graph[edge[0]] = append(graph[edge[0]], edge[1])
        graph[edge[1]] = append(graph[edge[1]], edge[0])
    }
    distance, queue := make([]int, n), [][]int{{0, 0}}
    distance[0] = -1
    for len(queue) > 0 {
        cur := queue[0]
        queue = queue[1:]
        for _, other := range graph[cur[0]] {
            if distance[other] == 0 {
                distance[other] = cur[1] + 1
                queue = append(queue, []int{other, cur[1] + 1})
            }
        }
    }
    for i := 1; i < n; i++ {
        d, p := distance[i] * 2, patience[i]
        ans = max(ans, (d - 1) / p * p + d + 1)
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
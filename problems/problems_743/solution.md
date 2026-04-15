# [Python/Java] 堆实现BFS or 记录每个节点最短到达时间

> Author: Benhao
> Date: 2021-08-02
> Upvotes: 21
> Tags: Java, Python, Python3

---

### 解题思路
按最小的时间依次BFS搜索整个图即可。

### 代码

```python3 []
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connect = defaultdict(lambda:defaultdict(int))
        for u,v,w in times:
            connect[u][v] = w
        q = [(0, k)]
        explored = set()
        while q:
            t, node = heapq.heappop(q)
            if node in explored:
                continue
            explored.add(node)
            if len(explored) == n:
                return t
            for other, tm in connect[node].items():
                if other not in explored:
                    heapq.heappush(q, (t+tm, other))
        return -1
```
```Java []
class Solution {
    Map<Integer, Map<Integer, Integer>> connect;
    public int networkDelayTime(int[][] times, int n, int k) {
        connect = new HashMap<>();
        for(int i=0;i<times.length;i++){
            int u = times[i][0], v = times[i][1], w = times[i][2];
            Map cur = connect.getOrDefault(u, new HashMap<>());
            cur.put(v, w);
            connect.put(u, cur);
        }
        PriorityQueue<int[]> q = new PriorityQueue<>((a,b)->{
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });
        q.add(new int[]{0, k});
        Set<Integer> explored = new HashSet<>();
        while(q.size() > 0){
            int[] cur = q.poll();
            int t = cur[0], node = cur[1];
            if(explored.contains(node))
                continue;
            explored.add(node);
            if(explored.size() == n)
                return t;
            if(connect.containsKey(node)){
                for(int other: connect.get(node).keySet()){
                    if(!explored.contains(other)){
                        int tm = connect.get(node).get(other);
                        q.add(new int[]{t+tm, other});
                    }
                }
            }
        }
        return -1;
    }
}
```
<br>
```python3 []
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connect = defaultdict(lambda:defaultdict(int))
        for u,v,w in times:
            connect[u][v] = w
        q = deque([k])
        explored = defaultdict(lambda:inf)
        explored[k] = 0
        while q:
            node = q.popleft()
            t = explored[node]            
            for other, tm in connect[node].items():
                if t + tm < explored[other]:
                    explored[other] = t + tm
                    q.append(other)
        return -1 if len(explored) < n else max(explored.values())
```
```java []
class Solution {
    Map<Integer, Map<Integer, Integer>> connect;
    public int networkDelayTime(int[][] times, int n, int k) {
        connect = new HashMap<>();
        for(int i=0;i<times.length;i++){
            int u = times[i][0], v = times[i][1], w = times[i][2];
            Map<Integer, Integer> cur = connect.getOrDefault(u, new HashMap<>());
            cur.put(v, w);
            connect.put(u, cur);
        }
        Deque<Integer> q = new ArrayDeque<>();
        q.add(k);
        Map<Integer, Integer> explored = new HashMap<>();
        explored.put(k, 0);
        while(!q.isEmpty()){
            int poll = q.pollFirst();
            int t = explored.get(poll);
            if(connect.containsKey(poll)){
                Map<Integer, Integer> cur = connect.get(poll);
                for(int other:cur.keySet()){
                    int tm = cur.get(other);
                    if(!explored.containsKey(other) || t+tm < explored.get(other)){
                        explored.put(other, t + tm);
                        q.add(other);
                    }
                }
            }
        }
        int max = 0;
        for(int i=1;i<=n;i++){
            if(!explored.containsKey(i))
                return -1;
            max = Math.max(max, explored.get(i));
        }
        return max;
    }
}
```

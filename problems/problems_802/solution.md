# [Python/Java] 以出度为0开始的拓扑排序 or 搜索

> Author: Benhao
> Date: 2021-08-04
> Upvotes: 21
> Tags: Java, Python, Python3

---

### 解题思路
拓扑的解法中，所有出度为0的点是安全的，那么出到这些点的点也可以减去这条边，如果其剩下的出度为0，它也是安全的，以此类推。

搜索的时候可以标记节点的当前状态，如果他有出口，暂定为1，如果他的出口全部为安全的点，他们的和必然为0，就认定它也是安全的，否则它是不安全的。

### 代码
拓扑
```Python3 []
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out = [0] * n
        edges = defaultdict(list)
        for i, nodes in enumerate(graph):
            for node in nodes:
                edges[node].append(i)
                # 统计所有点的出度
                out[i] += 1
        q = deque([])
        for i in range(n):
            if not out[i]:
                # 出度为0的点加入队列
                q.append(i)
        while q:
            node = q.popleft()
            for front in edges[node]:
                # 去掉front->node这条边
                out[front] -= 1
                if not out[front]:
                    # 如果去掉该边后front的出度变为0，加入队列
                    q.append(front)
        return [i for i in range(n) if not out[i]]
```
```Java []
class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        int[] out = new int[n];
        Map<Integer, List<Integer>> edges = new HashMap<>();
        for(int i=0;i<n;i++)
            for(int j:graph[i]){
                List<Integer> cur = edges.getOrDefault(j, new ArrayList<>());
                cur.add(i);
                edges.put(j, cur);
                out[i]++;
            }
        Deque<Integer> queue = new LinkedList<>();
        for(int i=0;i<n;i++)
            if(out[i]==0)
                queue.add(i);
        List<Integer> ans = new ArrayList<>();
        while(queue.size()>0){
            int node = queue.pollFirst();
            ans.add(node);
            if(edges.containsKey(node))
                for(int nxt: edges.get(node)){
                    out[nxt]--;
                    if(out[nxt] == 0)
                        queue.add(nxt);
                }
        }
        Collections.sort(ans);
        return ans;
    }
}
```
DFS
```Python3 []
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # 每个点可能的状态: -1:点是未走过的, 0:点是安全的，1:点是走过的不确定安不安全，2:点是不安全的
        states = [-1] * n

        def dfs(node):
            # 还未访问过
            if states[node] == -1:
                # 标记为状态1
                states[node] = 1
                for nxt in graph[node]:
                    states[node] += dfs(nxt)
                    # 已经知道是不安全的了,可以提前结束循环
                    if states[node] > 1:
                        break
                # 出的所有点为安全的，它才是安全的
                states[node] = 0 if states[node] == 1 else 2
            return states[node]

        return [i for i in range(n) if not dfs(i)]
```
```Java []
class Solution {
    int[][] graph_;
    int[] states;
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        // 每个点可能的状态: -1:点是未走过的, 0:点是安全的，1:点是走过的不确定安不安全，2:点是不安全的
        states = new int[n];
        Arrays.fill(states, -1);
        graph_ = graph;
        List<Integer> ans = new ArrayList<>();
        for(int i=0;i<n;i++)
            if(dfs(i)==0)
                ans.add(i);
        return ans;
    }

    public int dfs(int node){
        if(states[node] == -1){
            states[node] = 1;
            for(int nxt:graph_[node]){
                states[node] += dfs(nxt);
                if(states[node] > 1)
                    break;
            }
            if(states[node] == 1)
                states[node] = 0;
            else
                states[node] = 2;
        }
        return states[node];
    }
}
```
DFS也可以使用纯boolean来标记
```Python3 []
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # 每个点可能的状态: 安全的，不安全的
        states = [None] * n

        def dfs(node):
            if states[node] is None:
                states[node] = False
                if all(dfs(nxt) for nxt in graph[node]):
                    states[node] = True
            return states[node]
        
        return [i for i in range(n) if dfs(i)]
```
```Java []
class Solution {
    int[][] graph_;
    Map<Integer,Boolean> states;
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        graph_ = graph;
        states = new HashMap<>();
        List<Integer> ans = new ArrayList<>();
        for(int i=0;i<n;i++){
            if(safe(i))
                ans.add(i);
        }
        return ans;
    }

    public boolean safe(int node){
        if(!states.containsKey(node)){
            states.put(node, false);
            boolean allTrue = true;
            for(int nxt: graph_[node])
                if(!safe(nxt)){
                    allTrue = false;
                    break;
                }
            states.put(node, allTrue);
        }
        return states.get(node);
    }
}
```
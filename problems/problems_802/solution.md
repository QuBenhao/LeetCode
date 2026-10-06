# [Python/Java] Topological sort from nodes with outdegree 0, or search

> Author: Benhao
> Date: 2021-08-04
> Upvotes: 21
> Tags: Java, Python, Python3

---

### Approach
In the topological approach, every node with outdegree 0 is safe. Remove edges leading to these nodes; if a predecessor's remaining outdegree becomes 0, it is safe too. Repeat this process.

During search, mark each node's current state. If it has outgoing edges, tentatively assign 1. If all its successors are safe, their states sum to 0 and this node is safe too; otherwise it is unsafe.

### Code
Topological sort
```Python3 []
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out = [0] * n
        edges = defaultdict(list)
        for i, nodes in enumerate(graph):
            for node in nodes:
                edges[node].append(i)
                # Count every node's outdegree
                out[i] += 1
        q = deque([])
        for i in range(n):
            if not out[i]:
                # Enqueue nodes with outdegree 0
                q.append(i)
        while q:
            node = q.popleft()
            for front in edges[node]:
                # Remove the edge front->node
                out[front] -= 1
                if not out[front]:
                    # If removing the edge makes front's outdegree 0, enqueue it
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
        # Node states: -1: unvisited, 0: safe, 1: visited but safety undetermined, 2: unsafe
        states = [-1] * n

        def dfs(node):
            # Not yet visited
            if states[node] == -1:
                # Mark as state 1
                states[node] = 1
                for nxt in graph[node]:
                    states[node] += dfs(nxt)
                    # Already known to be unsafe; stop the loop early
                    if states[node] > 1:
                        break
                # A node is safe only if all its successors are safe
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
        // Node states: -1: unvisited, 0: safe, 1: visited but safety undetermined, 2: unsafe
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
DFS can also use boolean flags alone
```Python3 []
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # Node states: safe or unsafe
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

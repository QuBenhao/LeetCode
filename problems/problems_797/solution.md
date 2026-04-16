# [Python/Java] 记忆化dfs or BFS or 回溯

> Author: Benhao
> Date: 2021-08-24
> Upvotes: 47
> Tags: Java, Python, Python3

---

### 解题思路
无环图，我们从起点往每个点都走一遍到终点就行

### 代码

记忆化递归
```Python3 []
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        @lru_cache(None)
        def dfs(node):
            if node == n - 1:
                return [[n - 1]]
            ans = []
            for nxt in graph[node]:
                for res in dfs(nxt):
                    ans.append([node] + res)
            return ans
        
        return dfs(0)
```
```Java []
class Solution {
    int n;
    int[][] g;
    Map<Integer, List<List<Integer>>> cache;
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        n = graph.length;
        g = graph;
        cache = new HashMap<>();
        return dfs(0);
    }

    public List<List<Integer>> dfs(int node){
        if(cache.containsKey(node))
            return cache.get(node);
        List<List<Integer>> res = new ArrayList<>();
        if(node == n - 1){
            List<Integer> cur = new ArrayList<>(){{add(node);}};
            res.add(cur);
        }else{
            for(int nxt:g[node]){
                for(List<Integer> list:dfs(nxt)){
                    List<Integer> cur = new ArrayList(list);
                    cur.add(0, node);
                    res.add(cur);
                }
            }
        }
        cache.put(node, res);
        return res;
    }
}
```

BFS
```Python3 []
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        q = deque([[0]])
        ans = []
        while q:
            path = q.popleft()
            if path[-1] == n - 1:
                ans.append(path)
                continue
            for nxt in graph[path[-1]]:
                q.append(path + [nxt])
        return ans
```
```Java []
class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int n = graph.length;
        Queue<List<Integer>> q = new LinkedList<>();
        q.add(new ArrayList<>(){{add(0);}});
        List<List<Integer>> ans = new ArrayList<>();
        while(q.size() > 0){
            List<Integer> path = q.remove();
            int node = path.get(path.size() - 1);
            if(node == n - 1)
                ans.add(path);
            else
                for(int nxt: graph[node]){
                    List<Integer> nxt_path = new ArrayList<>(path);
                    nxt_path.add(nxt);
                    q.add(nxt_path);
                }
        }
        return ans;
    }
}
```

回溯
```Python3 []
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        path = [0]
        ans = []
        
        def backtracking():
            if path[-1] == n - 1:
                ans.append(list(path))
            else:
                for nxt in graph[path[-1]]:
                    path.append(nxt)
                    backtracking()
                    path.pop()
        
        backtracking()
        return ans
```
```Java []
class Solution {
    int n;
    Deque<Integer> path;
    List<List<Integer>> ans;
    int[][] g;
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        n = graph.length;
        path = new LinkedList<>(){{addLast(0);}};
        ans = new ArrayList<>();
        g = graph;
        backtracking();
        return ans;
    }

    public void backtracking(){
        int node = path.peekLast();
        if(node == n - 1)
            ans.add(new ArrayList(path));
        else{
            for(int nxt: g[node]){
                path.addLast(nxt);
                backtracking();
                path.pollLast();
            }
        }
    }
}
```
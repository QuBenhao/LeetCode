# [Python/Java] (状态压缩 or tuple) + BFS or 迭代加深深度优先搜索

> Author: Benhao
> Date: 2021-08-06
> Upvotes: 16
> Tags: Java, Python, Python3

---

### 解题思路
用一个长度为n的二进制表示每个点被走过的状态(该位为0表示没走过，该位为1表示走过)，我们最终的目标是走过所有点，也就是$2^n-1$。
**不会状态压缩也没有关系，利用Py的tuple记录走过的状态也可以，效果和二进制一样的，只是效率没那么高，但是通俗易懂（保证看得懂）。**


BFS初始起点从每个点开始，我们第一次走到终点的时候，所用的距离就是最终答案。


### 代码

```Python3 []
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # 初始以每个点为起点
        frontier = [(i, 1 << i) for i in range(n)]
        explored = set(frontier)
        # 目标为2^n - 1
        goal = (1 << n) - 1
        step = 0
        while frontier:
            nxt = []
            for cur, state in frontier:
                if state == goal:
                    return step
                for other in graph[cur]:
                    # 下一个状态
                    successor = (other, 1 << other | state)
                    # 新的状态没有被走过
                    if successor not in explored:
                        explored.add(successor)
                        nxt.append(successor)
            frontier = nxt
            step += 1
        # 图不连通
        return -1
```
```Java []
class Solution {
    public int shortestPathLength(int[][] graph) {
        int n = graph.length, goal;
        goal = (1 << n) - 1;
        Deque<int[]> q = new LinkedList<>();
        boolean[][] seen = new boolean[n][1<<n];
        for(int i=0;i<n;i++)
            q.add(new int[]{i,1<<i,0});
        while(!q.isEmpty()){
            int[] cur = q.pollFirst();
            if(cur[1] == goal)
                return cur[2];
            seen[cur[0]][cur[1]] = true;
            for(int other: graph[cur[0]]){
                int nxt = 1 << other | cur[1];
                if(!seen[other][nxt]){
                    q.add(new int[]{other, nxt, cur[2]+1});
                    seen[other][nxt] = true;
                }
            }
        }
        return -1;
    }
}
```

tuple
```python3
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        frontier = []
        temp = [0] * n
        for i in range(n):
            temp[i] = 1
            # 其实这个temp和1<<i表示的是完全相同的状态
            frontier.append((i, tuple(temp)))
            temp[i] = 0
        # 必须是tuple因为list是属于unhashable的
        explored = set(frontier)
        goal = tuple([1] * n)
        step = 0
        while frontier:
            nxt = []
            for cur, state in frontier:
                if state == goal:
                    return step
                for other in graph[cur]:
                    # 把一个tuple再转换成list，实际上也进行了复制
                    temp = list(state)
                    # 这就相当于 1 << other | state
                    temp[other] = 1
                    # 将list转换成tuple，这样可以hash判断有没有走过
                    successor = (other, tuple(temp))
                    if successor not in explored:
                        explored.add(successor)
                        nxt.append(successor)
            frontier = nxt
            step += 1
        # 图不连通
        return -1
```

【额外思路】迭代加深深度优先搜索
```Python3 []
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        @cache
        def id_dfs(i, state, d):
            if d == 0:
                return state == goal
            for j in graph[i]:
                if id_dfs(j, state|1<<j, d-1):
                    return True
            return False

        n = len(graph)
        goal = (1<<n)-1
        init = [1<<i for i in range(n)]
        depth = 0
        while True:
            for start in range(n):
                if id_dfs(start, init[start], depth):
                    return depth
            depth += 1
```
```Python3 []
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        @cache
        def id_dfs(i, state, d):
            if d == 0:
                return state == goal
            d -= 1
            return any(id_dfs(j, state | 1 << j, d) for j in graph[i])

        n = len(graph)
        goal = (1<<n)-1
        init = [1<<i for i in range(n)]
        depth = 0
        while True:
            if any(id_dfs(i, init[i], depth) for i in range(n)):
                return depth
            depth += 1
```
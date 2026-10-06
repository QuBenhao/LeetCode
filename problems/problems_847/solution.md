# [Python/Java] Bitmask or tuple + BFS, or iterative deepening depth-first search

> Author: Benhao
> Date: 2021-08-06
> Upvotes: 16
> Tags: Java, Python, Python3

---

### Approach
Use an n-bit binary number to record which nodes have been visited: 0 means unvisited and 1 means visited. The goal is to visit every node, represented by $2^n-1$.
**If you are unfamiliar with bitmasks, a Python tuple can record the visited state too. It works like the binary representation, though less efficiently, and is easy to understand (I promise).**


Start BFS from every node. The distance when we first reach the goal state is the answer.


### Code

```Python3 []
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # Initialize with every node as a starting point
        frontier = [(i, 1 << i) for i in range(n)]
        explored = set(frontier)
        # The goal is 2^n - 1
        goal = (1 << n) - 1
        step = 0
        while frontier:
            nxt = []
            for cur, state in frontier:
                if state == goal:
                    return step
                for other in graph[cur]:
                    # Next state
                    successor = (other, 1 << other | state)
                    # The new state has not been visited
                    if successor not in explored:
                        explored.add(successor)
                        nxt.append(successor)
            frontier = nxt
            step += 1
        # The graph is disconnected
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
            # temp represents exactly the same state as 1<<i
            frontier.append((i, tuple(temp)))
            temp[i] = 0
        # Must be a tuple because a list is unhashable
        explored = set(frontier)
        goal = tuple([1] * n)
        step = 0
        while frontier:
            nxt = []
            for cur, state in frontier:
                if state == goal:
                    return step
                for other in graph[cur]:
                    # Converting a tuple back to a list also makes a copy
                    temp = list(state)
                    # Equivalent to 1 << other | state
                    temp[other] = 1
                    # Convert the list to a tuple so hashing can check whether it has been visited
                    successor = (other, tuple(temp))
                    if successor not in explored:
                        explored.add(successor)
                        nxt.append(successor)
            frontier = nxt
            step += 1
        # The graph is disconnected
        return -1
```

[Additional approach] Iterative deepening depth-first search
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

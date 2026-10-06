# Topological sorting

```python
from collections import defaultdict, deque
def largestPathValue(colors, edges):
    """
    :type colors: str
    :type edges: List[List[int]]
    :rtype: int
    """
    """
    Topological sorting:
    Order all nodes of a directed graph so that no node points to a node that precedes it.
    First count the indegree of every node. Remove a node with indegree 0, then decrease the indegree of each node it points to by one.
    Repeat until all nodes have been removed.
    If nodes remain but none has indegree 0, the graph contains a cycle and has no topological ordering, which means there is no solution in many problems.
    """
    n = len(colors)
    # Indegree of each node
    degree = [0] * n
    graph = defaultdict(set)
    for a, b in edges:
        degree[b] += 1
        graph[a].add(b)

    # dp: maximum count of each color on reaching each node
    dp = [[0] * 26 for _ in range(n)]
    # Topological sorting
    q = [i for i in range(n) if not degree[i]]
    count = 0
    while q:
        count += 1
        i = q.pop()
        # On visiting node i, add its color
        dp[i][ord(colors[i]) - ord('a')] += 1
        for j in graph[i]:
            degree[j] -= 1
            # When moving from node i to node j, inherit each color count from i if it exceeds the current value
            for c in range(26):
                dp[j][c] = max(dp[j][c], dp[i][c])
            if degree[j] == 0:
                q.append(j)
    # The topological sort detected a cycle
    if count != n:
        return -1
    return max(max(dp[i]) for i in range(n))

```

```golang
package main

import (
    "container/list"
)

func largestPathValue(colors string, edges [][]int) (ans int) {
	n := len(colors)
	graph := make(map[int][]int)
	indegree := make([]int, n)
	for _, edge := range edges {
		u, v := edge[0], edge[1]
		graph[u] = append(graph[u], v)
		indegree[v]++
	}
	queue := list.New()
	for i, degree := range indegree {
		if degree == 0 {
			queue.PushBack(i)
		}
	}
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, 26)
	}
	count := 0
	for queue.Len() > 0 {
		node := queue.Front()
		queue.Remove(node)
		count++
		u := node.Value.(int)
		dp[u][colors[u]-'a']++
		ans = max(ans, dp[u][colors[u]-'a'])
		for _, v := range graph[u] {
			for i := range dp[v] {
				dp[v][i] = max(dp[v][i], dp[u][i])
			}
			indegree[v]--
			if indegree[v] == 0 {
				queue.PushBack(v)
			}
		}
	}
	if count < n {
		return -1 // Cycle detected
	}
	return
}
```

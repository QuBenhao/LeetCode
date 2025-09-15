# 拓扑排序

```python
from collections import defaultdict, deque
def largestPathValue(colors, edges):
    """
    :type colors: str
    :type edges: List[List[int]]
    :rtype: int
    """
    """
    拓扑排序:
    在一个有向图中，对所有的节点进行排序，要求没有一个节点指向它前面的节点。
    先统计所有节点的入度，对于入度为0的节点就可以分离出来，然后把这个节点指向的节点的入度减一。
    一直做改操作，直到所有的节点都被分离出来。
    如果最后不存在入度为0的节点，那就说明有环，不存在拓扑排序，也就是很多题目的无解的情况。
    """
    n = len(colors)
    # 每个点的入度
    degree = [0] * n
    graph = defaultdict(set)
    for a, b in edges:
        degree[b] += 1
        graph[a].add(b)

    # dp: 到达每个点时，每个颜色的最大值
    dp = [[0] * 26 for _ in range(n)]
    # 拓扑排序
    q = [i for i in range(n) if not degree[i]]
    count = 0
    while q:
        count += 1
        i = q.pop()
        # 我们访问到了节点i，加入节点i的颜色
        dp[i][ord(colors[i]) - ord('a')] += 1
        for j in graph[i]:
            degree[j] -= 1
            # 我们从节点i访问到了节点j,继承i的所有颜色 (如果超过当前值)
            for c in range(26):
                dp[j][c] = max(dp[j][c], dp[i][c])
            if degree[j] == 0:
                q.append(j)
    # 拓扑排序有环
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
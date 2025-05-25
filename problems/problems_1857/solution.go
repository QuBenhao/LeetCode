package problem1857

import (
	"container/list"
	"encoding/json"
	"log"
	"strings"
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

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var colors string
	var edges [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &colors); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}

	return largestPathValue(colors, edges)
}

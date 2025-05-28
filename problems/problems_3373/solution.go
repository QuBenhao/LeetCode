package problem3373

import (
	"encoding/json"
	"log"
	"strings"
)

func maxTargetNodes(edges1 [][]int, edges2 [][]int) []int {
	var buildGraph func([][]int) [][]int
	buildGraph = func(edges [][]int) [][]int {
		graph := make([][]int, len(edges)+1)
		for _, edge := range edges {
			u, v := edge[0], edge[1]
			graph[u] = append(graph[u], v)
			graph[v] = append(graph[v], u)
		}
		return graph
	}

	var dfs func([][]int, int, int, int) int
	dfs = func(graph [][]int, node int, parent int, d int) (res int) {
		if d == 0 {
			res++
		}
		for _, neighbor := range graph[node] {
			if neighbor != parent {
				res += dfs(graph, neighbor, node, d^1)
			}
		}
		return
	}

	graph1 := buildGraph(edges1)
	graph2 := buildGraph(edges2)
	m, n := len(graph1), len(graph2)

	tree2 := dfs(graph2, 0, -1, 1)
	max2 := max(tree2, n-tree2)
	ans := make([]int, m)
	ans[0] = dfs(graph1, 0, -1, 0) + max2

	var dfs2 func(int, int)
	dfs2 = func(node int, parent int) {
		for _, neighbor := range graph1[node] {
			if neighbor != parent {
				ans[neighbor] = m - ans[node] + max2*2
				dfs2(neighbor, node)
			}
		}
	}
	dfs2(0, -1)
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges1 [][]int
	var edges2 [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges2); err != nil {
		log.Fatal(err)
	}

	return maxTargetNodes(edges1, edges2)
}

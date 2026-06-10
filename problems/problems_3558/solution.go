package problem3558

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD int64 = 1e9 + 7

func fastpow(a, b int64) int {
	res := int64(1)
	a %= MOD
	for b > 0 {
		if (b & 1) == 1 {
			res = res * a % MOD
		}
		a = a * a % MOD
		b >>= 1
	}
	return int(res)
}

func assignEdgeWeights(edges [][]int) int {
	n := len(edges) + 1
	graph := make([][]int, n)
	for _, edge := range edges {
		u, v := edge[0]-1, edge[1]-1
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	var dfs func(int, int) int
	dfs = func(node, parent int) int {
		maxDepth := 0
		for _, child := range graph[node] {
			if child == parent {
				continue
			}
			maxDepth = max(maxDepth, dfs(child, node))
		}
		return maxDepth + 1
	}

	depth := dfs(0, -1) - 1
	return int(fastpow(2, int64(depth-1)))
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}

	return assignEdgeWeights(edges)
}

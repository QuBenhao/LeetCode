package problem3372

import (
	"encoding/json"
	"log"
	"strings"
)

func maxTargetNodes(edges1 [][]int, edges2 [][]int, k int) []int {
	var dfs func(map[int][]int, int, int, int) int
	dfs = func(graph map[int][]int, node int, pa int, left int) int {
		if left < 0 {
			return 0
		}
		if left == 0 {
			return 1
		}
		res := 1
		for _, nei := range graph[node] {
			if nei == pa {
				continue
			}
			res += dfs(graph, nei, node, left-1)
		}
		return res
	}
	graph1 := make(map[int][]int)
	for _, edge := range edges1 {
		graph1[edge[0]] = append(graph1[edge[0]], edge[1])
		graph1[edge[1]] = append(graph1[edge[1]], edge[0])
	}
	graph2 := make(map[int][]int)
	for _, edge := range edges2 {
		graph2[edge[0]] = append(graph2[edge[0]], edge[1])
		graph2[edge[1]] = append(graph2[edge[1]], edge[0])
	}
	max2 := 0
	for i := range len(edges2) + 1 {
		max2 = max(max2, dfs(graph2, i, -1, k-1))
	}
	ans := make([]int, len(edges1)+1)
	for i := range len(edges1) + 1 {
		ans[i] = max2 + dfs(graph1, i, -1, k)
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges1 [][]int
	var edges2 [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return maxTargetNodes(edges1, edges2, k)
}

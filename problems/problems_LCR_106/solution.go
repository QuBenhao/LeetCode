package problemLCR_106

import (
	"encoding/json"
	"log"
	"strings"
)

func isBipartite(graph [][]int) bool {
	n := len(graph)
	color := make([]int, n)
	for i := 0; i < n; i++ {
		color[i] = -1
	}
	var dfs func(int, int) bool
	dfs = func(node int, c int) bool {
		if color[node] != -1 {
			return color[node] == c
		}
		color[node] = c
		nxt := 1 ^ c
		for _, other := range graph[node] {
			if !dfs(other, nxt) {
				return false
			}
		}
		return true
	}
	for i := 0; i < n; i++ {
		if color[i] != -1 {
			continue
		}
		if !dfs(i, 0) {
			return false
		}
	}
	return true
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var graph [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &graph); err != nil {
		log.Fatal(err)
	}

	return isBipartite(graph)
}

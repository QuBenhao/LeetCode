package problemLCR_110

import (
	"encoding/json"
	"log"
	"strings"
)

func allPathsSourceTarget(graph [][]int) [][]int {
	var res [][]int
	var dfs func(int, []int)
	dfs = func(u int, path []int) {
		path = append(path, u)
		if u == len(graph)-1 {
			res = append(res, append([]int(nil), path...))
			return
		}
		for _, v := range graph[u] {
			dfs(v, path)
		}
	}
	dfs(0, []int{})
	return res
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var graph [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &graph); err != nil {
		log.Fatal(err)
	}

	return allPathsSourceTarget(graph)
}

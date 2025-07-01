package problem3331

import (
	"encoding/json"
	"log"
	"strings"
)

func findSubtreeSizes(parent []int, s string) []int {
	n := len(parent)
	graph := make([][]int, n)
	for i := 1; i < n; i++ {
		graph[parent[i]] = append(graph[parent[i]], i)
	}
	ans := make([]int, n)
	mapping := make([]int, 26)
	for i := range mapping {
		mapping[i] = -1
	}

	var dfs func(int)
	dfs = func(node int) {
		before := mapping[s[node]-'a']
		mapping[s[node]-'a'] = node
		for _, child := range graph[node] {
			dfs(child)
		}
		mapping[s[node]-'a'] = before
		ans[node]++
		if before != -1 {
			ans[before] += ans[node]
		} else if parent[node] != -1 {
			ans[parent[node]] += ans[node]
		}
	}
	dfs(0)
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var parent []int
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &parent); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &s); err != nil {
		log.Fatal(err)
	}

	return findSubtreeSizes(parent, s)
}

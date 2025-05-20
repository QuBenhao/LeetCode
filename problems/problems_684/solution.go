package problem684

import (
	"encoding/json"
	"log"
	"strings"
)

func findRedundantConnection(edges [][]int) []int {
	n := len(edges)
	parent := make([]int, n+1)
	for i := 0; i <= n; i++ {
		parent[i] = i
	}

	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}

	for _, edge := range edges {
		x, y := edge[0], edge[1]
		rootX, rootY := find(x), find(y)
		if rootX == rootY {
			return edge
		}
		parent[rootX] = rootY
	}
	return nil
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}

	return findRedundantConnection(edges)
}

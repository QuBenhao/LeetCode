package problem3068

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

type pair struct {
	x int64
	y int64
}

func maximumValueSum(nums []int, k int, edges [][]int) int64 {
	graph := make(map[int][]int)
	for _, edge := range edges {
		graph[edge[0]] = append(graph[edge[0]], edge[1])
		graph[edge[1]] = append(graph[edge[1]], edge[0])
	}

	var dfs func(int, int) pair
	dfs = func(node, parent int) pair {
		var f0, f1 int64
		f1 = math.MinInt64
		for _, neigh := range graph[node] {
			if neigh == parent {
				continue
			}
			child := dfs(neigh, node)
			f0, f1 = max(f0+child.x, f1+child.y), max(f0+child.y, f1+child.x)
		}
		return pair{
			max(f0+int64(nums[node]), f1+int64(nums[node]^k)),
			max(f1+int64(nums[node]), f0+int64(nums[node]^k)),
		}
	}
	return dfs(0, -1).x
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int
	var edges [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &edges); err != nil {
		log.Fatal(err)
	}

	return maximumValueSum(nums, k, edges)
}

package problem2322

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minimumScore(nums []int, edges [][]int) int {
	n := len(nums)
	graph := make([][]int, n)
	for _, edge := range edges {
		u, v := edge[0], edge[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	xors := make([]int, n)
	timeIn := make([]int, n)
	timeOut := make([]int, n)
	var timer int
	var dfs func(int, int) int
	dfs = func(node, parent int) int {
		xors[node] = nums[node]
		timeIn[node] = timer
		timer++
		for _, neighbor := range graph[node] {
			if neighbor != parent {
				xors[node] ^= dfs(neighbor, node)
			}
		}
		timeOut[node] = timer
		timer++
		return xors[node]
	}
	dfs(0, -1)

	ans := math.MaxInt32
	for x := 1; x < n-1; x++ {
		for y := x + 1; y < n; y++ {
			var a, b, c int
			if timeIn[x] < timeIn[y] && timeOut[y] < timeOut[x] {
				a = xors[y]
				b = xors[x] ^ a
				c = xors[0] ^ xors[x]
			} else if timeIn[y] < timeIn[x] && timeOut[x] < timeOut[y] {
				a = xors[x]
				b = xors[y] ^ a
				c = xors[0] ^ xors[y]
			} else {
				a = xors[x]
				b = xors[y]
				c = xors[0] ^ a ^ b
			}
			ans = min(ans, max(a, max(b, c))-min(a, min(b, c)))
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var edges [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}

	return minimumScore(nums, edges)
}

package problem3629

import (
	"encoding/json"
	"log"
	"strings"
)

var MAX_N = 1000001
var PRIME_FACTORS = make([][]int, MAX_N)

func init() {
	for i := 2; i < MAX_N; i++ {
		if len(PRIME_FACTORS[i]) == 0 {
			for j := i; j < MAX_N; j += i {
				PRIME_FACTORS[j] = append(PRIME_FACTORS[j], i)
			}
		}
	}
}

func minJumps(nums []int) int {
	n := len(nums)
	graph := map[int][]int{}
	for i, num := range nums {
		for _, factor := range PRIME_FACTORS[num] {
			graph[factor] = append(graph[factor], i)
		}
	}
	visited := make([]bool, n)
	queue := []int{0}
	visited[0] = true
	steps := 0
	for len(queue) > 0 {
		sz := len(queue)
		for i := range sz {
			idx := queue[i]
			if idx == n-1 {
				return steps
			}
			nextIndices := graph[nums[idx]]
			nextIndices = append(nextIndices, idx+1)
			if idx > 0 {
				nextIndices = append(nextIndices, idx-1)
			}
			for _, nextIdx := range nextIndices {
				if !visited[nextIdx] {
					visited[nextIdx] = true
					queue = append(queue, nextIdx)
				}
			}
		}
		queue = queue[sz:]
		steps++
	}
	return -1
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return minJumps(nums)
}

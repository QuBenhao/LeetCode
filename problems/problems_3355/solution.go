package problem3355

import (
	"encoding/json"
	"log"
	"strings"
)

func isZeroArray(nums []int, queries [][]int) bool {
	n := len(nums)
	diff := make([]int, n+1)
	for _, query := range queries {
		diff[query[0]]++
		diff[query[1]+1]--
	}
	s := 0
	for i := range n {
		s += diff[i]
		if s < nums[i] {
			return false
		}
	}
	return true
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return isZeroArray(nums, queries)
}

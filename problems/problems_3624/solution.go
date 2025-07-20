package problem3624

import (
	"encoding/json"
	"log"
	"strings"
)

func popcountDepth(nums []int64, queries [][]int64) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int64
	var queries [][]int64

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return popcountDepth(nums, queries)
}

package problem3068

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumValueSum(nums []int, k int, edges [][]int) int64 {
    
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

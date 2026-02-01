package problem3013

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumCost(nums []int, k int, dist int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int
	var dist int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &dist); err != nil {
		log.Fatal(err)
	}

	return minimumCost(nums, k, dist)
}

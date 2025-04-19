package problem2563

import (
	"encoding/json"
	"log"
	"strings"
)

func countFairPairs(nums []int, lower int, upper int) int64 {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var lower int
	var upper int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &lower); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &upper); err != nil {
		log.Fatal(err)
	}

	return countFairPairs(nums, lower, upper)
}

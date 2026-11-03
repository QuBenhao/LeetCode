package problem3505

import (
	"encoding/json"
	"log"
	"strings"
)

func minOperations(nums []int, x int, k int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var x int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &x); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return minOperations(nums, x, k)
}

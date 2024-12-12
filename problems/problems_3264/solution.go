package problem3264

import (
	"encoding/json"
	"log"
	"strings"
)

func getFinalState(nums []int, k int, multiplier int) []int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int
	var multiplier int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &multiplier); err != nil {
		log.Fatal(err)
	}

	return getFinalState(nums, k, multiplier)
}

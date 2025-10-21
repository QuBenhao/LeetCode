package problem3347

import (
	"encoding/json"
	"log"
	"strings"
)

func maxFrequency(nums []int, k int, numOperations int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int
	var numOperations int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &numOperations); err != nil {
		log.Fatal(err)
	}

	return maxFrequency(nums, k, numOperations)
}

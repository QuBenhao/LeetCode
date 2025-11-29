package problem1590

import (
	"encoding/json"
	"log"
	"strings"
)

func minSubarray(nums []int, p int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var p int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &p); err != nil {
		log.Fatal(err)
	}

	return minSubarray(nums, p)
}

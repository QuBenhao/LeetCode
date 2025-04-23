package problem2799

import (
	"encoding/json"
	"log"
	"strings"
)

func countCompleteSubarrays(nums []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countCompleteSubarrays(nums)
}

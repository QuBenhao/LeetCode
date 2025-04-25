package problem2444

import (
	"encoding/json"
	"log"
	"strings"
)

func countSubarrays(nums []int, minK int, maxK int) int64 {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var minK int
	var maxK int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &minK); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &maxK); err != nil {
		log.Fatal(err)
	}

	return countSubarrays(nums, minK, maxK)
}

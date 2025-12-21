package problem3785

import (
	"encoding/json"
	"log"
	"strings"
)

func minSwaps(nums []int, forbidden []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var forbidden []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &forbidden); err != nil {
		log.Fatal(err)
	}

	return minSwaps(nums, forbidden)
}

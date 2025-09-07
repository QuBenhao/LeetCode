package problem3674

import (
	"encoding/json"
	"log"
	"strings"
)

func minOperations(nums []int) int {
	for _, num := range nums {
		if num != nums[0] {
			return 1
		}
	}
	return 0
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return minOperations(nums)
}

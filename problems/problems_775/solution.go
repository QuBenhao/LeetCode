package problem775

import (
	"encoding/json"
	"log"
	"strings"
)

func isIdealPermutation(nums []int) bool {
	for i := range nums {
		if d := nums[i] - i; d < -1 || d > 1 {
			return false
		}
	}
	return true
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return isIdealPermutation(nums)
}

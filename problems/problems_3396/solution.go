package problem3396

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumOperations(nums []int) int {
	s := make(map[int]any, len(nums))
	for i := len(nums) - 1; i >= 0; i-- {
		if _, ok := s[nums[i]]; ok {
			return i/3 + 1
		}
		s[nums[i]] = nil
	}
	return 0
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return minimumOperations(nums)
}

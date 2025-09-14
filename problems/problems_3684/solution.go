package problem3684

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func maxKDistinct(nums []int, k int) []int {
	slices.SortFunc(nums, func(a, b int) int {
		return b - a
	})
	nums = slices.Compact(nums)
	if len(nums) > k {
		return nums[:k]
	}
	return nums
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maxKDistinct(nums, k)
}

package problem2563

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func countFairPairs(nums []int, lower int, upper int) (ans int64) {
	slices.Sort(nums)
	left, right := len(nums)-1, len(nums)-1
	for i, num := range nums {
		left_bound, right_bound := lower-num, upper-num
		for right > i && nums[right] > right_bound {
			right--
		}
		for left > i && nums[left] >= left_bound {
			left--
		}
		ans += int64(max(right, i) - max(left, i))
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var lower int
	var upper int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &lower); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &upper); err != nil {
		log.Fatal(err)
	}

	return countFairPairs(nums, lower, upper)
}

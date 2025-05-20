package problem34

import (
	"encoding/json"
	"log"
	"strings"
)

func searchRange(nums []int, target int) []int {
	bisectLeft := func(nums []int, target int) int {
		l, r := 0, len(nums)
		for l < r {
			mid := l + (r-l)/2
			if nums[mid] < target {
				l = mid + 1
			} else {
				r = mid
			}
		}
		return l
	}
	bisectRight := func(nums []int, target int) int {
		l, r := 0, len(nums)
		for l < r {
			mid := l + (r-l)/2
			if nums[mid] <= target {
				l = mid + 1
			} else {
				r = mid
			}
		}
		return l
	}
	lIdx, rIdx := bisectLeft(nums, target), bisectRight(nums, target)-1
	if lIdx <= rIdx && rIdx < len(nums) && nums[lIdx] == target {
		return []int{lIdx, rIdx}
	}
	return []int{-1, -1}
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return searchRange(nums, target)
}

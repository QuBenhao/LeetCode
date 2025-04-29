package problem81

import (
	"encoding/json"
	"log"
	"strings"
)

func binarySearch(nums []int, left, right, target int) int {
	l, r := left, right
	for l < r {
		mid := l + (r-l)/2
		if nums[mid] < target {
			l = mid + 1
		} else {
			r = mid
		}
	}
	if nums[r] == target {
		return r
	}
	return -1
}

func search(nums []int, target int) bool {
	n := len(nums)
	left, right := 0, n-1
	// 恢复二段性
	for left < right && nums[right] == nums[left] {
		right--
	}
	for left < right {
		mid := left + (right-left+1)/2
		if nums[mid] >= nums[0] {
			left = mid
		} else {
			right = mid - 1
		}
	}
	idx := n
	if nums[right] >= nums[0] && right < n-1 {
		idx = right + 1
	}
	if target >= nums[0] {
		return binarySearch(nums, 0, idx-1, target) != -1
	} else {
		return binarySearch(nums, idx, n-1, target) != -1
	}
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return search(nums, target)
}

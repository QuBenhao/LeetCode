package problemLCR_070

import (
	"encoding/json"
	"log"
	"strings"
)

func singleNonDuplicate(nums []int) int {
	left, right := 0, len(nums)-1
	for left < right {
		mid := left + (right-left)/2
		if nums[mid] == nums[mid^1] {
			left = (mid | 1) + 1
		} else {
			right = mid
		}
	}
	return nums[left]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return singleNonDuplicate(nums)
}

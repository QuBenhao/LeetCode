package problem300

import (
	"encoding/json"
	"log"
	"strings"
)

func lengthOfLIS(nums []int) int {
	stack := []int{nums[0]}
	for i := 1; i < len(nums); i++ {
		if nums[i] > stack[len(stack)-1] {
			stack = append(stack, nums[i])
		} else {
			l, r := 0, len(stack)-1
			for l < r {
				m := l + (r-l)/2
				if stack[m] < nums[i] {
					l = m + 1
				} else {
					r = m
				}
			}
			stack[l] = nums[i]
		}
	}
	return len(stack)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return lengthOfLIS(nums)
}

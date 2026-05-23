package problem1752

import (
	"encoding/json"
	"log"
	"strings"
)

func check(nums []int) bool {
	n, decr := len(nums), false
	for i := range nums {
		if nums[i] > nums[(i+1)%n] {
			if decr {
				return false
			}
			decr = true
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

	return check(nums)
}

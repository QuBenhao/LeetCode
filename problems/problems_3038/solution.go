package problem3038

import (
	"encoding/json"
	"log"
	"strings"
)

func maxOperations(nums []int) int {
	for i, s := 2, nums[0]+nums[1]; i < len(nums)-1; i += 2 {
		if nums[i]+nums[i+1] != s {
			return i / 2
		}
	}
	return len(nums) / 2
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxOperations(nums)
}

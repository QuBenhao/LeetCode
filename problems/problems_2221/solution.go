package problem2221

import (
	"encoding/json"
	"log"
	"strings"
)

func triangularSum(nums []int) int {
	n := len(nums)
	for i := n - 1; i > 0; i-- {
		for j := range i {
			nums[j] = (nums[j] + nums[j+1]) % 10
		}
	}
	return nums[0]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return triangularSum(nums)
}

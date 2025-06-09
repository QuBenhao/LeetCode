package problem3196

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumTotalCost(nums []int) int64 {
	n := len(nums)
	f0, f1 := int64(nums[0]), int64(nums[0])
	for i := 1; i < n; i++ {
		f0, f1 = f1-int64(nums[i]), max(f0, f1)+int64(nums[i])
	}
	return max(f0, f1)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maximumTotalCost(nums)
}

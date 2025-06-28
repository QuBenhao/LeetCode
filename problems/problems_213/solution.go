package problem213

import (
	"encoding/json"
	"log"
	"strings"
)

func robHelper(nums []int, start int, end int) int {
	rob, notRob := nums[start], 0
	for i := start + 1; i <= end; i++ {
		newRob := notRob + nums[i]
		notRob = max(rob, notRob)
		rob = newRob
	}
	return max(rob, notRob)
}

func rob(nums []int) int {
	n := len(nums)
	if n == 1 {
		return nums[0]
	}
	return max(robHelper(nums, 0, n-2), robHelper(nums, 1, n-1))
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return rob(nums)
}

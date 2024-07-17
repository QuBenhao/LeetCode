package problem198

import (
	"encoding/json"
	"log"
	"strings"
)

func rob(nums []int) int {
	dp0, dp1 := 0, nums[0]
	for i := 1; i < len(nums); i++ {
		dp0, dp1 = max(dp0, dp1), max(dp0+nums[i], dp1)
	}
	return max(dp0, dp1)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return rob(nums)
}

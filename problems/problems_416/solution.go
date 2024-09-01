package problem416

import (
	"encoding/json"
	"log"
	"strings"
)

func canPartition(nums []int) bool {
	s := 0
	for _, num := range nums {
		s += num
	}
	if s%2 != 0 {
		return false
	}
	target := s / 2
	dp := make([]bool, target+1)
	dp[0] = true
	for _, num := range nums {
		for i := target; i >= num; i-- {
			dp[i] = dp[i] || dp[i-num]
		}
	}
	return dp[target]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return canPartition(nums)
}

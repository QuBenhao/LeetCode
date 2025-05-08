package problemLCR_101

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
	if s%2 == 1 {
		return false
	}
	s /= 2
	dp := make([]bool, s+1)
	dp[0] = true
	for _, num := range nums {
		for i := s; i >= num; i-- {
			dp[i] = dp[i] || dp[i-num]
		}
	}
	return dp[s]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return canPartition(nums)
}

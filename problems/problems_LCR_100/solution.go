package problemLCR_100

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumTotal(triangle [][]int) int {
	n := len(triangle)
	dp := make([]int, n)
	for i, nums := range triangle {
		if i > 0 {
			dp[i] = dp[i-1] + nums[i]
		}
		for j := i - 1; j > 0; j-- {
			dp[j] = min(dp[j], dp[j-1]) + nums[j]
		}
		dp[0] += nums[0]
	}
	ans := dp[0]
	for i := 1; i < n; i++ {
		ans = min(ans, dp[i])
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var triangle [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &triangle); err != nil {
		log.Fatal(err)
	}

	return minimumTotal(triangle)
}

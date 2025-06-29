package problem3599

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minXor(nums []int, k int) int {
	n := len(nums)
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, k+1)
		for j := range dp[i] {
			dp[i][j] = math.MaxInt32
		}
	}
	preXor := make([]int, n+1)
	for i := range n {
		preXor[i+1] = preXor[i] ^ nums[i]
	}
	dp[0][0] = 0
	for i := range n {
		dp[i+1][1] = preXor[i+1]
	}
	for i := range n {
		for j := 2; j <= k; j++ {
			for l := j - 1; l <= i; l++ {
				xorValue := preXor[i+1] ^ preXor[l]
				dp[i+1][j] = min(dp[i+1][j], max(dp[l][j-1], xorValue))
			}
		}
	}
	return dp[n][k]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return minXor(nums, k)
}

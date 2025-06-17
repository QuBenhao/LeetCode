package problem813

import (
	"encoding/json"
	"log"
	"strings"
)

func largestSumOfAverages(nums []int, k int) float64 {
	n := len(nums)
	prefixSum := make([]float64, n+1)
	for i, num := range nums {
		prefixSum[i+1] = prefixSum[i] + float64(num)
	}
	dp := make([][]float64, n+1)
	for i := range dp {
		dp[i] = make([]float64, k+1)
	}
	for i := range n {
		for j := 1; j <= min(i+1, k); j++ {
			if j == 1 {
				dp[i+1][j] = (prefixSum[i+1] - prefixSum[0]) / float64(i+1)
				continue
			}
			for l := j - 1; l <= i; l++ {
				dp[i+1][j] = max(dp[i+1][j], dp[l][j-1]+(prefixSum[i+1]-prefixSum[l])/float64(i+1-l))
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

	return largestSumOfAverages(nums, k)
}

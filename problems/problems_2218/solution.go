package problem2218

import (
	"encoding/json"
	"log"
	"strings"
)

func maxValueOfCoins(piles [][]int, k int) int {
	n := len(piles)
	prefixSum := make([][]int, n)
	for i, pile := range piles {
		prefixSum[i] = make([]int, len(pile)+1)
		for j, p := range pile {
			prefixSum[i][j+1] = prefixSum[i][j] + p
		}
	}
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, k+1)
	}
	for i := range min(k, len(piles[0])) + 1 {
		dp[0][i] = prefixSum[0][i]
	}
	s := len(piles[0])
	for i := 1; i < n; i++ {
		s += len(piles[i])
		for j := range min(k, s) + 1 {
			for pick := range min(j, len(piles[i])) + 1 {
				dp[i][j] = max(dp[i][j], dp[i-1][j-pick]+prefixSum[i][pick])
			}
		}
	}
	return dp[n-1][k]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var piles [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &piles); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maxValueOfCoins(piles, k)
}

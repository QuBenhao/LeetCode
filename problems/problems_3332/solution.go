package problem3332

import (
	"encoding/json"
	"log"
	"strings"
)

func maxScore(n int, k int, stayScore [][]int, travelScore [][]int) (ans int) {
	dp := make([][]int, 2)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for i := range k {
		for j := range n {
			for jj := range n {
				if j == jj {
					dp[(i+1)%2][j] = max(dp[(i+1)%2][j], dp[i%2][j]+stayScore[i][j])
				} else {
					dp[(i+1)%2][jj] = max(dp[(i+1)%2][jj], dp[i%2][j]+travelScore[j][jj])
				}
			}
		}
	}
	for i := range n {
		ans = max(ans, dp[k%2][i])
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var k int
	var stayScore [][]int
	var travelScore [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &stayScore); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &travelScore); err != nil {
		log.Fatal(err)
	}

	return maxScore(n, k, stayScore, travelScore)
}

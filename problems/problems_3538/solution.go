package problem3538

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minTravelTime(l int, n int, k int, position []int, time []int) int {
	prefixTime := make([]int, n+1)
	for i, t := range time {
		prefixTime[i+1] = prefixTime[i] + t
	}
	dp := make([][][]int, k+1)
	for i := range dp {
		dp[i] = make([][]int, n+1)
		for j := 0; j <= n; j++ {
			dp[i][j] = make([]int, n+1)
		}
	}
	for leftK := 1; leftK <= k; leftK++ {
		// range: integer values from zero to an upper limit [Go 1.22]
		for pre := range n {
			dp[leftK][n-1][pre] = math.MaxInt >> 1
		}
	}
	for leftK := range dp {
		for i := n - 2; i >= 0; i-- {
			for pre := range i + 1 {
				t := prefixTime[i+1] - prefixTime[pre]
				res := math.MaxInt
				for nxt := i + 1; nxt < min(n, i+2+leftK); nxt++ {
					res = min(res, dp[leftK-(nxt-i-1)][nxt][i+1]+t*(position[nxt]-position[i]))
				}
				dp[leftK][i][pre] = res
			}
		}
	}
	return dp[k][0][0]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var l int
	var n int
	var k int
	var position []int
	var time []int

	if err := json.Unmarshal([]byte(inputValues[0]), &l); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &position); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &time); err != nil {
		log.Fatal(err)
	}

	return minTravelTime(l, n, k, position, time)
}

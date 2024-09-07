package problemLCR_093

import (
	"encoding/json"
	"log"
	"strings"
)

func lenLongestFibSubseq(arr []int) (ans int) {
	n := len(arr)
	idx := map[int]int{}
	for i, x := range arr {
		idx[x] = i
	}
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			nxt := arr[i] + arr[j]
			if k, has := idx[nxt]; has && k > j {
				dp[j][k] = dp[i][j] + 1
				ans = max(ans, dp[j][k]+2)
			}
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return lenLongestFibSubseq(arr)
}

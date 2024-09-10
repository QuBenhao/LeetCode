package problem2555

import (
	"encoding/json"
	"log"
	"strings"
)

func maximizeWin(prizePositions []int, k int) (ans int) {
	n := len(prizePositions)
	dp := make([]int, n+1)
	left := 0
	for right, p := range prizePositions {
		for prizePositions[left] < p-k {
			left++
		}
		dp[right+1] = max(dp[right], right-left+1)
		ans = max(ans, dp[left]+right-left+1)
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var prizePositions []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &prizePositions); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maximizeWin(prizePositions, k)
}

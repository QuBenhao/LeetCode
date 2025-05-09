package problem2209

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumWhiteTiles(floor string, numCarpets int, carpetLen int) int {
	n := len(floor)
	if numCarpets*carpetLen >= n {
		return 0
	}
	dp := [2][]int{}
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	for i := range floor {
		dp[0][i+1] = dp[0][i] + int(floor[i]-'0')
	}
	for i := 1; i <= numCarpets; i++ {
		for j := i * carpetLen; j <= n; j++ {
			dp[i%2][j] = min(dp[i%2][j-1]+dp[0][j]-dp[0][j-1], dp[(i+1)%2][j-carpetLen])
		}
	}
	return dp[numCarpets%2][n]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var floor string
	var numCarpets int
	var carpetLen int

	if err := json.Unmarshal([]byte(inputValues[0]), &floor); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &numCarpets); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &carpetLen); err != nil {
		log.Fatal(err)
	}

	return minimumWhiteTiles(floor, numCarpets, carpetLen)
}

package problem3363

import (
	"encoding/json"
	"log"
	"strings"
)

func maxCollectedFruits(fruits [][]int) (ans int) {
	n := len(fruits)
	ans = fruits[0][0] + fruits[n-1][n-1]
	dp1 := make([]int, n+1)
	dp2 := make([]int, n+1)
	dp1[n-1] = fruits[0][n-1]
	dp2[n-1] = fruits[n-1][0]
	for i := 1; i < n-1; i++ {
		ans += fruits[i][i]
		nextDp1 := make([]int, n+1)
		nextDp2 := make([]int, n+1)
		for j := max(n-1-i, i+1); j < n; j++ {
			nextDp1[j] = max(max(dp1[j-1], dp1[j]), dp1[j+1]) + fruits[i][j]
			nextDp2[j] = max(max(dp2[j-1], dp2[j]), dp2[j+1]) + fruits[j][i]
		}
		dp1 = nextDp1
		dp2 = nextDp2
	}
	ans += dp1[n-1] + dp2[n-1]
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var fruits [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &fruits); err != nil {
		log.Fatal(err)
	}

	return maxCollectedFruits(fruits)
}

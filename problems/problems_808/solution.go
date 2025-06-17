package problem808

import (
	"encoding/json"
	"log"
	"strings"
)

// func init() {
// 	for i := range 5000 {
// 		if soupServings(i+1) >= 0.99999 {
// 			log.Printf("soupServings(%d) >= 0.99999\n", i)
// 			// n超过4451以后已经和1的误差在10^-5以内
// 			break
// 		}
// 	}
// }

func soupServings(n int) float64 {
	if n == 0 {
		return 0.5 // 当A和B都为0时，返回0.5
	}
	n = (n + 24) / 25 // Round up to the nearest multiple of 25
	if n >= 178 {
		return 1.0
	}
	dp := make([][]float64, n+1)
	for i := range dp {
		dp[i] = make([]float64, n+1)
	}
	dp[0][0] = 0.5 // 当A和B都为0时，返回0.5
	dp[0][1] = 1.0 // 当A为0，B为1时，返回1.0
	for i := range n {
		for j := range n {
			dp[0][j+1] = 1.0                  // 当A为0，B大于0时，返回1.0
			a := dp[max(0, i-3)][j+1]         // A消耗4，B不消耗
			b := dp[max(0, i-2)][max(0, j)]   // A消耗3，B消耗1
			c := dp[max(0, i-1)][max(0, j-1)] // A消耗2，B消耗2
			d := dp[max(0, i)][max(0, j-2)]   // A消耗1，B消耗3
			dp[i+1][j+1] = (a + b + c + d) / 4.0
		}
	}
	return dp[n][n]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return soupServings(n)
}

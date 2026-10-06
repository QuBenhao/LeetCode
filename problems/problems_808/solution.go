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
// 			// Once n exceeds 4451, the difference from 1 is within 10^-5
// 			break
// 		}
// 	}
// }

func soupServings(n int) float64 {
	if n == 0 {
		return 0.5 // Return 0.5 when both A and B are 0
	}
	n = (n + 24) / 25 // Round up to the nearest multiple of 25
	if n >= 178 {
		return 1.0
	}
	dp := make([][]float64, n+1)
	for i := range dp {
		dp[i] = make([]float64, n+1)
	}
	dp[0][0] = 0.5 // Return 0.5 when both A and B are 0
	dp[0][1] = 1.0 // Return 1.0 when A is 0 and B is 1
	for i := range n {
		for j := range n {
			dp[0][j+1] = 1.0                  // Return 1.0 when A is 0 and B is positive
			a := dp[max(0, i-3)][j+1]         // Consume 4 from A and none from B
			b := dp[max(0, i-2)][max(0, j)]   // Consume 3 from A and 1 from B
			c := dp[max(0, i-1)][max(0, j-1)] // Consume 2 from A and 2 from B
			d := dp[max(0, i)][max(0, j-2)]   // Consume 1 from A and 3 from B
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

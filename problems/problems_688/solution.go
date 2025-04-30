package problem688

import (
	"encoding/json"
	"log"
	"strings"
)

func knightProbability(n int, k int, row int, column int) float64 {
	dirs := [][]int{{-1, -2}, {-1, 2}, {1, -2}, {1, 2}, {-2, -1}, {-2, 1}, {2, -1}, {2, 1}}
	dp := make([][][]float64, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][]float64, n)
		for j := 0; j < n; j++ {
			dp[i][j] = make([]float64, 2)
			dp[i][j][0] = 1
		}
	}
	for p := 1; p <= k; p++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				dp[i][j][p%2] = 0
				for _, dir := range dirs {
					nx, ny := i+dir[0], j+dir[1]
					if nx < 0 || nx >= n || ny < 0 || ny >= n {
						continue
					}
					dp[i][j][p%2] += dp[nx][ny][(p+1)%2] / 8
				}
			}
		}
	}
	return dp[row][column][k%2]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var k int
	var row int
	var column int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &row); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &column); err != nil {
		log.Fatal(err)
	}

	return knightProbability(n, k, row, column)
}

package problem799

import (
	"encoding/json"
	"log"
	"strings"
)

func champagneTower(poured int, query_row int, query_glass int) float64 {
	dp := []float64{float64(poured)}
	for i := 1; i <= query_row; i++ {
		next_dp := make([]float64, i+1)
		for j := 0; j < i; j++ {
			if dp[j] > 1 {
				excess := (dp[j] - 1) / 2
				next_dp[j] += excess
				next_dp[j+1] += excess
			}
		}
		dp = next_dp
	}
	return min(1.0, dp[query_glass])
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var poured int
	var query_row int
	var query_glass int

	if err := json.Unmarshal([]byte(inputValues[0]), &poured); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &query_row); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &query_glass); err != nil {
		log.Fatal(err)
	}

	return champagneTower(poured, query_row, query_glass)
}

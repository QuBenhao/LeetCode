package problem871

import (
	"encoding/json"
	"log"
	"strings"
)

func minRefuelStops(target int, startFuel int, stations [][]int) int {
	n := len(stations)
	dp := make([]int, n+1)
	dp[0] = startFuel
	for i := 0; i < n; i++ {
		for t := i; t >= 0; t-- {
			if dp[t] >= stations[i][0] {
				dp[t+1] = max(dp[t+1], dp[t]+stations[i][1])
			}
		}
	}
	for i := 0; i <= n; i++ {
		if dp[i] >= target {
			return i
		}
	}
	return -1
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var target int
	var startFuel int
	var stations [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &target); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &startFuel); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &stations); err != nil {
		log.Fatal(err)
	}

	return minRefuelStops(target, startFuel, stations)
}

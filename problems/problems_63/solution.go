package problem63

import (
	"encoding/json"
	"log"
	"strings"
)

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	n := len(obstacleGrid[0])
	dp := make([]int, n)
	dp[0] = 1
	for _, obstacles := range obstacleGrid {
		for j, obstacle := range obstacles {
			if obstacle == 0 {
				if j > 0 {
					dp[j] += dp[j-1]
				}
			} else {
				dp[j] = 0
			}
		}
	}
	return dp[n-1]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var obstacleGrid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &obstacleGrid); err != nil {
		log.Fatal(err)
	}

	return uniquePathsWithObstacles(obstacleGrid)
}

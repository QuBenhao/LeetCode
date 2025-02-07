package problem63

import (
	"encoding/json"
	"log"
	"strings"
)

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var obstacleGrid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &obstacleGrid); err != nil {
		log.Fatal(err)
	}

	return uniquePathsWithObstacles(obstacleGrid)
}

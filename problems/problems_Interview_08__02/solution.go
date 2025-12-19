package problemInterview_08__02

import (
	"encoding/json"
	"log"
	"strings"
)

func pathWithObstacles(obstacleGrid [][]int) [][]int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var obstacleGrid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &obstacleGrid); err != nil {
		log.Fatal(err)
	}

	return pathWithObstacles(obstacleGrid)
}

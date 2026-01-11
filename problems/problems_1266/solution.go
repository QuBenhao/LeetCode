package problem1266

import (
	"encoding/json"
	"log"
	"strings"
)

func minTimeToVisitAllPoints(points [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var points [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &points); err != nil {
		log.Fatal(err)
	}

	return minTimeToVisitAllPoints(points)
}

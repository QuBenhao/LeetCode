package problem3286

import (
	"encoding/json"
	"log"
	"strings"
)

func findSafeWalk(grid [][]int, health int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int
	var health int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &health); err != nil {
		log.Fatal(err)
	}

	return findSafeWalk(grid, health)
}

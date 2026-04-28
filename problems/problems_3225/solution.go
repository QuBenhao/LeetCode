package problem3225

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumScore(grid [][]int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return maximumScore(grid)
}

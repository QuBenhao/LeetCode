package problem3195

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumArea(grid [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return minimumArea(grid)
}

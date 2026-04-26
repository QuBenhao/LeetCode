package problem1391

import (
	"encoding/json"
	"log"
	"strings"
)

func hasValidPath(grid [][]int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return hasValidPath(grid)
}

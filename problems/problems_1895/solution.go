package problem1895

import (
	"encoding/json"
	"log"
	"strings"
)

func largestMagicSquare(grid [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return largestMagicSquare(grid)
}

package problem1277

import (
	"encoding/json"
	"log"
	"strings"
)

func countSquares(matrix [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	return countSquares(matrix)
}

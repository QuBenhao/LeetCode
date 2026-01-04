package problem1975

import (
	"encoding/json"
	"log"
	"strings"
)

func maxMatrixSum(matrix [][]int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	return maxMatrixSum(matrix)
}

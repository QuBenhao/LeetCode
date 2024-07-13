package problem74

import (
	"encoding/json"
	"log"
	"strings"
)

func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 {
		return false
	}

	row, col := 0, len(matrix[0])-1
	for row < len(matrix) && col >= 0 {
		if matrix[row][col] == target {
			return true
		}
		if matrix[row][col] > target {
			col--
		} else {
			row++
		}
	}
	return false
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix [][]int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &matrix); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return searchMatrix(matrix, target)
}

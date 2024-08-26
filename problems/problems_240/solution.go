package problem240

import (
	"encoding/json"
	"log"
	"strings"
)

func searchMatrix(matrix [][]int, target int) bool {
	m, n := len(matrix), len(matrix[0])
	row, col := m-1, 0
	for row >= 0 && col < n {
		if matrix[row][col] == target {
			return true
		} else if matrix[row][col] > target {
			row--
		} else {
			col++
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

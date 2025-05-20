package problem73

import (
	"encoding/json"
	"log"
	"strings"
)

func setZeroes(matrix [][]int) {
	m, n := len(matrix), len(matrix[0])
	firstCol, firstRow := false, false
	for i := 0; i < m; i++ {
		if matrix[i][0] == 0 {
			firstCol = true
			break
		}
	}
	for i := 0; i < n; i++ {
		if matrix[0][i] == 0 {
			firstRow = true
			break
		}
	}
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[i][j] == 0 {
				matrix[i][0] = 0
				matrix[0][j] = 0
			}
		}
	}
	for i := 1; i < m; i++ {
		if matrix[i][0] == 0 {
			for j := 1; j < n; j++ {
				matrix[i][j] = 0
			}
		}
	}
	for j := 1; j < n; j++ {
		if matrix[0][j] == 0 {
			for i := 1; i < m; i++ {
				matrix[i][j] = 0
			}
		}
	}
	if firstCol {
		for i := 0; i < m; i++ {
			matrix[i][0] = 0
		}
	}
	if firstRow {
		for j := 0; j < n; j++ {
			matrix[0][j] = 0
		}
	}
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var matrix [][]int

	if err := json.Unmarshal([]byte(values[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	setZeroes(matrix)
	return matrix
}

package problem3033

import (
	"encoding/json"
	"log"
	"strings"
)

func modifiedMatrix(matrix [][]int) [][]int {
	for m, n, j := len(matrix), len(matrix[0]), 0; j < n; j++ {
		mx := -1
		var remain []int
		for i := 0; i < m; i++ {
			if matrix[i][j] != -1 {
				mx = max(mx, matrix[i][j])
			} else {
				remain = append(remain, i)
			}
		}
		for _, i := range remain {
			matrix[i][j] = mx
		}
	}
	return matrix
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	return modifiedMatrix(matrix)
}

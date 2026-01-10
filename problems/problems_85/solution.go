package problem85

import (
	"encoding/json"
	"log"
	"strings"
)

func maximalRectangle(matrix [][]byte) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix [][]byte

	var matrixStr [][]string
	if err := json.Unmarshal([]byte(inputValues[0]), &matrixStr); err != nil {
		log.Fatal(err)
	}
	matrix = make([][]byte, len(matrixStr))
	for i := 0; i < len(matrix); i++ {
		matrix[i] = make([]byte, len(matrixStr[i]))
		for j := 0; j < len(matrix[i]); j++ {
			matrix[i][j] = matrixStr[i][j][0]
		}
	}

	return maximalRectangle(matrix)
}

func byteArrToStrArr(arr [][]byte) []string {
	ans := make([]string, len(arr))
	for i, b := range arr {
		ans[i] = string(b)
	}
	return ans
}

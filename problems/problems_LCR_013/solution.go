package problemLCR_013

import (
	"encoding/json"
	"log"
	"strings"
)

type NumMatrix struct {
	prefixSum [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	m, n := len(matrix), len(matrix[0])
	prefixSum := make([][]int, m+1)
	for i := range prefixSum {
		prefixSum[i] = make([]int, n+1)
	}
	for i := range m {
		for j := range n {
			prefixSum[i+1][j+1] = prefixSum[i][j+1] + prefixSum[i+1][j] - prefixSum[i][j] + matrix[i][j]
		}
	}
	return NumMatrix{prefixSum: prefixSum}
}

func (numMatrix *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	return numMatrix.prefixSum[row2+1][col2+1] - numMatrix.prefixSum[row1][col2+1] - numMatrix.prefixSum[row2+1][col1] + numMatrix.prefixSum[row1][col1]
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]any
	var ans []any
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	var matrixArr [][]int
	if v, ok := opValues[0][0].([][]int); ok {
		matrixArr = v
	} else {
		matrixArr = make([][]int, len(opValues[0][0].([]any)))
		for i := range matrixArr {
			matrixArr[i] = make([]int, len(opValues[0][0].([]any)[i].([]any)))
			for j := range matrixArr[i] {
				matrixArr[i][j] = int(opValues[0][0].([]any)[i].([]any)[j].(float64))
			}
		}
	}
	obj := Constructor(matrixArr)
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "sumRegion", "SumRegion":
			res = obj.SumRegion(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)), int(opValues[i][2].(float64)), int(opValues[i][3].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}

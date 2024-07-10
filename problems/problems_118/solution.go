package problem118

import (
	"encoding/json"
	"log"
	"strings"
)

func generate(numRows int) [][]int {
	ans := make([][]int, numRows)
	for i := 0; i < numRows; i++ {
		ans[i] = make([]int, i+1)
		ans[i][0], ans[i][i] = 1, 1
		for j := 1; j < i/2+1; j++ {
			ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
			ans[i][i-j] = ans[i][j]
		}
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var numRows int

	if err := json.Unmarshal([]byte(inputValues[0]), &numRows); err != nil {
		log.Fatal(err)
	}

	return generate(numRows)
}

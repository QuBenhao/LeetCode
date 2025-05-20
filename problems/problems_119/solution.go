package problem119

import (
	"encoding/json"
	"log"
	"strings"
)

func getRow(rowIndex int) []int {
	ans := make([]int, rowIndex+1)
	ans[0] = 1
	for i := 0; i <= rowIndex; i++ {
		half := i / 2
		for j := half; j > 0; j-- {
			ans[j] += ans[j-1]
		}
		if rowIndex > 0 {
			ans[half+1] = ans[half]
		}
	}
	for j := rowIndex/2 + 1; j <= rowIndex; j++ {
		ans[j] = ans[rowIndex-j]
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var rowIndex int

	if err := json.Unmarshal([]byte(inputValues[0]), &rowIndex); err != nil {
		log.Fatal(err)
	}

	return getRow(rowIndex)
}

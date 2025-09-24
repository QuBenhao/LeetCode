package problem120

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumTotal(triangle [][]int) int {
	n := len(triangle)
	for i := 1; i < n; i++ {
		for j := 1; j < i; j++ {
			triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
		}
		triangle[i][i] += triangle[i-1][i-1]
		triangle[i][0] += triangle[i-1][0]
	}
	ans := triangle[n-1][0]
	for i := 1; i < n; i++ {
		ans = min(ans, triangle[n-1][i])
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var triangle [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &triangle); err != nil {
		log.Fatal(err)
	}

	return minimumTotal(triangle)
}

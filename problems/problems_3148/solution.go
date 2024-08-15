package problem3148

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func maxScore(grid [][]int) int {
	ans := math.MinInt
	colsMin := make([]int, len(grid[0]))
	for i := 0; i < len(colsMin); i++ {
		colsMin[i] = math.MaxInt
	}
	for _, row := range grid {
		preMin := math.MaxInt
		for j, v := range row {
			ans = max(ans, v-min(preMin, colsMin[j]))
			colsMin[j] = min(colsMin[j], v)
			preMin = min(preMin, colsMin[j])
		}
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return maxScore(grid)
}

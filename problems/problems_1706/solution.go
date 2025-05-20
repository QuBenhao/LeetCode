package problem1706

import (
	"encoding/json"
	"log"
	"strings"
)

func findBall(grid [][]int) []int {
	m, n := len(grid), len(grid[0])
	ans := make([]int, n)
	for j := range n {
		curCol := j
		for i := range m {
			d := grid[i][curCol]
			curCol += d
			if curCol < 0 || curCol == n || grid[i][curCol] != d {
				curCol = -1
				break
			}
		}
		ans[j] = curCol
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return findBall(grid)
}

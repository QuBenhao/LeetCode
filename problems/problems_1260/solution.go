package problem1260

import (
	"encoding/json"
	"log"
	"strings"
)

func shiftGrid(grid [][]int, k int) [][]int {
	m, n := len(grid), len(grid[0])
	k %= m * n
	if k == 0 {
		return grid
	}
	ans := make([][]int, m)
	for i := range ans {
		ans[i] = make([]int, n)
	}
	x, y := k/n, k%n
	for _, row := range grid {
		for _, val := range row {
			ans[x][y] = val
			if y++; y == n {
				y = 0
				x++
			}
			x %= m
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return shiftGrid(grid, k)
}

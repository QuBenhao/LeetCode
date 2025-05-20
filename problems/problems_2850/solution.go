package problem2850

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minimumMoves(grid [][]int) int {
	var source, target [][]int
	for i, row := range grid {
		for j, val := range row {
			if val > 1 {
				for k := 0; k < val-1; k++ {
					source = append(source, []int{i, j})
				}
			} else if val == 0 {
				target = append(target, []int{i, j})
			}
		}
	}
	ans := math.MaxInt
	permute(source, 0, func() {
		total := 0
		for i, s := range source {
			total += abs(s[0]-target[i][0]) + abs(s[1]-target[i][1])
		}
		ans = min(ans, total)
	})
	return ans
}

func permute(source [][]int, idx int, f func()) {
	if idx == len(source) {
		f()
		return
	}
	for i := idx; i < len(source); i++ {
		source[idx], source[i] = source[i], source[idx]
		permute(source, idx+1, f)
		source[idx], source[i] = source[i], source[idx]
	}
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return minimumMoves(grid)
}

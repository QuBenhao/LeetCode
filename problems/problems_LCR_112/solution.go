package problemLCR_112

import (
	"encoding/json"
	"log"
	"maps"
	"slices"
	"strings"
)

var dirs = [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func longestIncreasingPath(matrix [][]int) (ans int) {
	m, n := len(matrix), len(matrix[0])
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	idxMap := make(map[int][][2]int)
	for i, row := range matrix {
		for j, val := range row {
			idxMap[val] = append(idxMap[val], [2]int{i, j})
		}
	}
	sortedVals := slices.Sorted(maps.Keys(idxMap))
	for _, val := range sortedVals {
		for _, pos := range idxMap[val] {
			i, j := pos[0], pos[1]
			for _, dir := range dirs {
				if ni, nj := i+dir[0], j+dir[1]; ni >= 0 && ni < m && nj >= 0 && nj < n && matrix[ni][nj] < val {
					dp[i][j] = max(dp[i][j], dp[ni][nj])
				}
			}
			dp[i][j]++
			ans = max(ans, dp[i][j])
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	return longestIncreasingPath(matrix)
}

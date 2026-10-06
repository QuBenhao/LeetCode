package problem2713

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func maxIncreasingCells(mat [][]int) int {
	type pair struct{ x, y int }
	g := map[int][]pair{}
	for i, row := range mat {
		for j, x := range row {
			g[x] = append(g[x], pair{i, j}) // Group equal elements and record their positions
		}
	}
	keys := make([]int, 0, len(g))
	for k := range g {
		keys = append(keys, k)
	}
	slices.Sort(keys)

	rowMax := make([]int, len(mat))
	colMax := make([]int, len(mat[0]))
	for _, x := range keys {
		pos := g[x]
		// Compute all f values before updating rowMax and colMax
		fs := make([]int, len(pos))
		for i, p := range pos {
			fs[i] = max(rowMax[p.x], colMax[p.y]) + 1
		}
		for i, p := range pos {
			rowMax[p.x] = max(rowMax[p.x], fs[i]) // Update the maximum f value in row p.x
			colMax[p.y] = max(colMax[p.y], fs[i]) // Update the maximum f value in column p.y
		}
	}
	return slices.Max(rowMax)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var mat [][]int

	if err := json.Unmarshal([]byte(values[0]), &mat); err != nil {
		log.Fatal(err)
	}

	return maxIncreasingCells(mat)
}

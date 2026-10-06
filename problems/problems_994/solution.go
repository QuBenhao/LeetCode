package problem994

import (
	"encoding/json"
	"log"
	"strings"
)

type pair struct{ x, y int }

var directions = []pair{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} // Four directions

func orangesRotting(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	fresh := 0
	q := []pair{}
	for i, row := range grid {
		for j, x := range row {
			if x == 1 {
				fresh++ // Count fresh oranges
			} else if x == 2 {
				q = append(q, pair{i, j}) // Oranges that are rotten initially
			}
		}
	}

	ans := -1
	for len(q) > 0 {
		ans++ // One minute passes
		tmp := q
		q = []pair{}
		for _, p := range tmp { // Oranges already rotten
			for _, d := range directions { // Four directions
				i, j := p.x+d.x, p.y+d.y
				if 0 <= i && i < m && 0 <= j && j < n && grid[i][j] == 1 { // Fresh orange
					fresh--
					grid[i][j] = 2 // Turn into a rotten orange
					q = append(q, pair{i, j})
				}
			}
		}
	}

	if fresh > 0 {
		return -1
	}
	return max(ans, 0)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(values[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return orangesRotting(grid)
}

package problem994

import (
	"encoding/json"
	"log"
	"strings"
)

type pair struct{ x, y int }

var directions = []pair{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} // 四方向

func orangesRotting(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	fresh := 0
	q := []pair{}
	for i, row := range grid {
		for j, x := range row {
			if x == 1 {
				fresh++ // 统计新鲜橘子个数
			} else if x == 2 {
				q = append(q, pair{i, j}) // 一开始就腐烂的橘子
			}
		}
	}

	ans := -1
	for len(q) > 0 {
		ans++ // 经过一分钟
		tmp := q
		q = []pair{}
		for _, p := range tmp { // 已经腐烂的橘子
			for _, d := range directions { // 四方向
				i, j := p.x+d.x, p.y+d.y
				if 0 <= i && i < m && 0 <= j && j < n && grid[i][j] == 1 { // 新鲜橘子
					fresh--
					grid[i][j] = 2 // 变成腐烂橘子
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

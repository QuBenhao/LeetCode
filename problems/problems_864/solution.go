package problem864

import (
	"encoding/json"
	"log"
	"strings"
)

var DIRS = [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func shortestPathAllKeys(grid []string) int {
	m, n := len(grid), len(grid[0])
	var queue [][3]int
	goals := 0
	visited := make([][][]bool, m)
	blocked := make([][]bool, m)
	for i, row := range grid {
		visited[i] = make([][]bool, n)
		blocked[i] = make([]bool, n)
		for j, c := range row {
			visited[i][j] = make([]bool, 1<<6) // 64 possible states for keys
			if c == '@' {
				queue = append(queue, [3]int{i, j, 0})
				visited[i][j][0] = true
			} else if c == '#' {
				blocked[i][j] = true
			} else if 'a' <= c && c <= 'f' {
				goals |= 1 << (c - 'a')
			}
		}
	}
	for steps := 0; len(queue) > 0; steps++ {
		size := len(queue)
		for i := range size {
			x, y, keys := queue[i][0], queue[i][1], queue[i][2]
			if keys == goals {
				return steps
			}
			for _, dir := range DIRS {
				nx, ny := x+dir[0], y+dir[1]
				if nx < 0 || nx >= m || ny < 0 || ny >= n || blocked[nx][ny] {
					continue
				}
				c := grid[nx][ny]
				if 'A' <= c && c <= 'F' && (keys&(1<<(c-'A'))) == 0 {
					continue // can't go through locked door
				}
				newKeys := keys
				if 'a' <= c && c <= 'f' {
					newKeys |= 1 << (c - 'a') // collect key
					if newKeys == goals {
						return steps + 1 // collected all keys
					}
				}
				if !visited[nx][ny][newKeys] {
					visited[nx][ny][newKeys] = true
					queue = append(queue, [3]int{nx, ny, newKeys})
				}
			}
		}
		queue = queue[size:]
	}
	return -1
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid []string

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return shortestPathAllKeys(grid)
}

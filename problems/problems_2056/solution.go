package problem2056

import (
	"encoding/json"
	"log"
	"strings"
)

type move struct {
	x0, y0 int // start
	dx, dy int // dir
	step   int // steps
}

const SIZE = 8

var DIRECTIONS = [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}}
var DM = map[byte][][]int{'r': DIRECTIONS[:4], 'b': DIRECTIONS[4:], 'q': DIRECTIONS}

func generateMoves(pieces []string, positions [][]int, idx int) (ans []move) {
	x0, y0 := positions[idx][0], positions[idx][1]
	ans = append(ans, move{x0, y0, 0, 0, 0})
	for _, d := range DM[pieces[idx][0]] {
		dx, dy := d[0], d[1]
		for s := 1; s < SIZE; s++ {
			if nx, ny := x0+dx*s, y0+dy*s; nx < 1 || nx > SIZE || ny < 1 || ny > SIZE {
				break
			}
			ans = append(ans, move{x0, y0, dx, dy, s})
		}
	}
	return
}

func isValid(m1, m2 move) bool {
	x1, y1 := m1.x0, m1.y0
	x2, y2 := m2.x0, m2.y0
	for i := range max(m1.step, m2.step) {
		if i < m1.step {
			x1 += m1.dx
			y1 += m1.dy
		}
		if i < m2.step {
			x2 += m2.dx
			y2 += m2.dy
		}
		if x1 == x2 && y1 == y2 {
			return false
		}
	}
	return true
}

func countCombinations(pieces []string, positions [][]int) (ans int) {
	n := len(pieces)
	allMoves := make([][]move, n)
	for i := range n {
		allMoves[i] = generateMoves(pieces, positions, i)
	}
	path := make([]move, n)
	var dfs func(int)
	dfs = func(i int) {
		if i == n {
			ans++
			return
		}
	outer:
		for _, move1 := range allMoves[i] {
			for _, move2 := range path[:i] {
				if !isValid(move1, move2) {
					continue outer
				}
			}
			path[i] = move1
			dfs(i + 1)
		}

	}
	dfs(0)
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var pieces []string
	var positions [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &pieces); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &positions); err != nil {
		log.Fatal(err)
	}

	return countCombinations(pieces, positions)
}

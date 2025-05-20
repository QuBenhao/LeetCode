package problem1275

import (
	"encoding/json"
	"log"
	"strings"
)

func tictactoe(moves [][]int) string {
	validRow := func(indexes []int) bool {
		meet := false
		for i := 0; i < 4 && !meet; i++ {
			meet = true
			for _, idx := range indexes {
				if i <= 1 && moves[idx][i] != moves[indexes[0]][i] {
					meet = false
					break
				} else if i == 2 && moves[idx][0] != moves[idx][1] {
					meet = false
					break
				} else if i == 3 && moves[idx][0]+moves[idx][1] != 2 {
					meet = false
					break
				}
			}
		}
		return meet
	}
	combinationCheck := func(start int) bool {
		for i := start; i < len(moves); i += 2 {
			for j := i + 2; j < len(moves); j += 2 {
				for k := j + 2; k < len(moves); k += 2 {
					if validRow([]int{i, j, k}) {
						return true
					}
				}
			}
		}
		return false
	}

	if combinationCheck(0) {
		return "A"
	}
	if combinationCheck(1) {
		return "B"
	}
	if len(moves) == 9 {
		return "Draw"
	}
	return "Pending"
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var moves [][]int

	if err := json.Unmarshal([]byte(values[0]), &moves); err != nil {
		log.Fatal(err)
	}

	return tictactoe(moves)
}

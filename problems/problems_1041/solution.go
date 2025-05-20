package problem1041

import (
	"encoding/json"
	"log"
	"strings"
)

func isRobotBounded(instructions string) bool {
	DIRS := [][]int{{0, 1}, {-1, 0}, {0, -1}, {1, 0}}
	x, y, d := 0, 0, 0
	for i := 0; i < len(instructions); i++ {
		switch instructions[i] {
		case 'L':
			d = (d + 1) % 4
			break
		case 'R':
			d = (d + 3) % 4
			break
		default:
			x += DIRS[d][0]
			y += DIRS[d][1]
		}
	}
	return (x == 0 && y == 0) || d != 0
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var instructions string

	if err := json.Unmarshal([]byte(values[0]), &instructions); err != nil {
		log.Fatal(err)
	}

	return isRobotBounded(instructions)
}

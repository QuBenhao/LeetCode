package problem657

import (
	"encoding/json"
	"log"
	"strings"
)

func judgeCircle(moves string) bool {
	horizontal, vertical := 0, 0
	for _, c := range moves {
		switch c {
		case 'U':
			vertical++
		case 'D':
			vertical--
		case 'L':
			horizontal--
		case 'R':
			horizontal++
		}
	}
	return horizontal == 0 && vertical == 0
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var moves string

	if err := json.Unmarshal([]byte(values[0]), &moves); err != nil {
		log.Fatal(err)
	}

	return judgeCircle(moves)
}

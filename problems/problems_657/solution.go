package problem657

import (
	"encoding/json"
	"log"
	"strings"
)

func judgeCircle(moves string) bool {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var moves string

	if err := json.Unmarshal([]byte(values[0]), &moves); err != nil {
		log.Fatal(err)
	}

	return judgeCircle(moves)
}

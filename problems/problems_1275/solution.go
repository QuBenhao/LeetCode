package problem1275

import (
	"encoding/json"
	"log"
	"strings"
)

func tictactoe(moves [][]int) string {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var moves [][]int

	if err := json.Unmarshal([]byte(values[0]), &moves); err != nil {
		log.Fatal(err)
	}

	return tictactoe(moves)
}

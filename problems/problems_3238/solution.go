package problem3238

import (
	"encoding/json"
	"log"
	"strings"
)

func winningPlayerCount(n int, pick [][]int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var pick [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &pick); err != nil {
		log.Fatal(err)
	}

	return winningPlayerCount(n, pick)
}

package problem2225

import (
	"encoding/json"
	"log"
	"strings"
)

func findWinners(matches [][]int) [][]int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var matches [][]int

	if err := json.Unmarshal([]byte(values[0]), &matches); err != nil {
		log.Fatal(err)
	}

	return findWinners(matches)
}

package problem2545

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func sortTheStudents(score [][]int, k int) [][]int {
	slices.SortFunc(score, func(a, b []int) int { return b[k] - a[k] })
	return score
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var score [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &score); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return sortTheStudents(score, k)
}

package problem3553

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumWeight(edges [][]int, queries [][]int) []int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges [][]int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return minimumWeight(edges, queries)
}

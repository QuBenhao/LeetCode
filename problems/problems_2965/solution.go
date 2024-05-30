package problem2965

import (
	"encoding/json"
	"log"
	"strings"
)

func findMissingAndRepeatedValues(grid [][]int) []int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(values[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return findMissingAndRepeatedValues(grid)
}

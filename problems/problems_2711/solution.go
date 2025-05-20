package problem2711

import (
	"encoding/json"
	"log"
	"strings"
)

func differenceOfDistinctValues(grid [][]int) [][]int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return differenceOfDistinctValues(grid)
}

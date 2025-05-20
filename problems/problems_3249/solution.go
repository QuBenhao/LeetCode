package problem3249

import (
	"encoding/json"
	"log"
	"strings"
)

func countGoodNodes(edges [][]int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}

	return countGoodNodes(edges)
}

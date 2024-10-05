package problemLCR_110

import (
	"encoding/json"
	"log"
	"strings"
)

func allPathsSourceTarget(graph [][]int) [][]int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var graph [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &graph); err != nil {
		log.Fatal(err)
	}

	return allPathsSourceTarget(graph)
}

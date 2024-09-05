package problemLCR_106

import (
	"encoding/json"
	"log"
	"strings"
)

func isBipartite(graph [][]int) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var graph [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &graph); err != nil {
		log.Fatal(err)
	}

	return isBipartite(graph)
}

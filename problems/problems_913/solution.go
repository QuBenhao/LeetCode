package problem913

import (
	"encoding/json"
	"log"
	"strings"
)

func catMouseGame(graph [][]int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var graph [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &graph); err != nil {
		log.Fatal(err)
	}

	return catMouseGame(graph)
}

package problem913

import (
	"encoding/json"
	"log"
	"strings"
)

func catMouseGame(graph [][]int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var graph [][]int

	if err := json.Unmarshal([]byte(values[0]), &graph); err != nil {
		log.Fatal(err)
	}

	return catMouseGame(graph)
}

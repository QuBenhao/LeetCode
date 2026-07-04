package problem1301

import (
	"encoding/json"
	"log"
	"strings"
)

func pathsWithMaxScore(board []string) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var board []string

	if err := json.Unmarshal([]byte(inputValues[0]), &board); err != nil {
		log.Fatal(err)
	}

	return pathsWithMaxScore(board)
}

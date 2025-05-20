package problem3552

import (
	"encoding/json"
	"log"
	"strings"
)

func minMoves(matrix []string) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix []string

	if err := json.Unmarshal([]byte(inputValues[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	return minMoves(matrix)
}

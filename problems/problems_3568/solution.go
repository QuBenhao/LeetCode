package problem3568

import (
	"encoding/json"
	"log"
	"strings"
)

func minMoves(classroom []string, energy int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var classroom []string
	var energy int

	if err := json.Unmarshal([]byte(inputValues[0]), &classroom); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &energy); err != nil {
		log.Fatal(err)
	}

	return minMoves(classroom, energy)
}

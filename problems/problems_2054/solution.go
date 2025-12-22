package problem2054

import (
	"encoding/json"
	"log"
	"strings"
)

func maxTwoEvents(events [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var events [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &events); err != nil {
		log.Fatal(err)
	}

	return maxTwoEvents(events)
}

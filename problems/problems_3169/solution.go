package problem3169

import (
	"encoding/json"
	"log"
	"strings"
)

func countDays(days int, meetings [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var days int
	var meetings [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &days); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &meetings); err != nil {
		log.Fatal(err)
	}

	return countDays(days, meetings)
}

package problem3414

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumWeight(intervals [][]int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var intervals [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &intervals); err != nil {
		log.Fatal(err)
	}

	return maximumWeight(intervals)
}

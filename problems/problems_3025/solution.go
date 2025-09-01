package problem3025

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfPairs(points [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var points [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &points); err != nil {
		log.Fatal(err)
	}

	return numberOfPairs(points)
}

package problem2492

import (
	"encoding/json"
	"log"
	"strings"
)

func minScore(n int, roads [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var roads [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &roads); err != nil {
		log.Fatal(err)
	}

	return minScore(n, roads)
}

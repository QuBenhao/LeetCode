package problem3495

import (
	"encoding/json"
	"log"
	"strings"
)

func minOperations(queries [][]int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &queries); err != nil {
		log.Fatal(err)
	}

	return minOperations(queries)
}

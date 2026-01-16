package problem3047

import (
	"encoding/json"
	"log"
	"strings"
)

func largestSquareArea(bottomLeft [][]int, topRight [][]int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var bottomLeft [][]int
	var topRight [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &bottomLeft); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &topRight); err != nil {
		log.Fatal(err)
	}

	return largestSquareArea(bottomLeft, topRight)
}

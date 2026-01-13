package problem3454

import (
	"encoding/json"
	"log"
	"strings"
)

func separateSquares(squares [][]int) float64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var squares [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &squares); err != nil {
		log.Fatal(err)
	}

	return separateSquares(squares)
}

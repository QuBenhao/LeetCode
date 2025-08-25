package problem3000

import (
	"encoding/json"
	"log"
	"strings"
)

func areaOfMaxDiagonal(dimensions [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var dimensions [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &dimensions); err != nil {
		log.Fatal(err)
	}

	return areaOfMaxDiagonal(dimensions)
}

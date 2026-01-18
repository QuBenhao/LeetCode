package problem1292

import (
	"encoding/json"
	"log"
	"strings"
)

func maxSideLength(mat [][]int, threshold int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var mat [][]int
	var threshold int

	if err := json.Unmarshal([]byte(inputValues[0]), &mat); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &threshold); err != nil {
		log.Fatal(err)
	}

	return maxSideLength(mat, threshold)
}

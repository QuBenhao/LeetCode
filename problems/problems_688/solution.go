package problem688

import (
	"encoding/json"
	"log"
	"strings"
)

func knightProbability(n int, k int, row int, column int) float64 {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var k int
	var row int
	var column int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &row); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &column); err != nil {
		log.Fatal(err)
	}

	return knightProbability(n, k, row, column)
}

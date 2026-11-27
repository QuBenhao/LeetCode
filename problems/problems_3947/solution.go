package problem3947

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumSaleItems(items [][]int, budget int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var items [][]int
	var budget int

	if err := json.Unmarshal([]byte(inputValues[0]), &items); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &budget); err != nil {
		log.Fatal(err)
	}

	return maximumSaleItems(items, budget)
}

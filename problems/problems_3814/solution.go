package problem3814

import (
	"encoding/json"
	"log"
	"strings"
)

func maxCapacity(costs []int, capacity []int, budget int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var costs []int
	var capacity []int
	var budget int

	if err := json.Unmarshal([]byte(inputValues[0]), &costs); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &capacity); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &budget); err != nil {
		log.Fatal(err)
	}

	return maxCapacity(costs, capacity, budget)
}

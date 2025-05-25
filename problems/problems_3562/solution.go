package problem3562

import (
	"encoding/json"
	"log"
	"strings"
)

func maxProfit(n int, present []int, future []int, hierarchy [][]int, budget int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var present []int
	var future []int
	var hierarchy [][]int
	var budget int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &present); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &future); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &hierarchy); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &budget); err != nil {
		log.Fatal(err)
	}

	return maxProfit(n, present, future, hierarchy, budget)
}

package problem1928

import (
	"encoding/json"
	"log"
	"strings"
)

func minCost(maxTime int, edges [][]int, passingFees []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var maxTime int
	var edges [][]int
	var passingFees []int

	if err := json.Unmarshal([]byte(inputValues[0]), &maxTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &passingFees); err != nil {
		log.Fatal(err)
	}

	return minCost(maxTime, edges, passingFees)
}

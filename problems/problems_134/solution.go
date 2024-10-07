package problem134

import (
	"encoding/json"
	"log"
	"strings"
)

func canCompleteCircuit(gas []int, cost []int) int {
	n := len(gas)
	totalTank, currTank := 0, 0
	start := 0
	for i := 0; i < n; i++ {
		totalTank += gas[i] - cost[i]
		currTank += gas[i] - cost[i]
		if currTank < 0 {
			start = i + 1
			currTank = 0
		}
	}
	if totalTank >= 0 {
		return start
	}
	return -1
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var gas []int
	var cost []int

	if err := json.Unmarshal([]byte(inputValues[0]), &gas); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &cost); err != nil {
		log.Fatal(err)
	}

	return canCompleteCircuit(gas, cost)
}

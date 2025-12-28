package problem3789

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumCost(cost1 int, cost2 int, costBoth int, need1 int, need2 int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var cost1 int
	var cost2 int
	var costBoth int
	var need1 int
	var need2 int

	if err := json.Unmarshal([]byte(inputValues[0]), &cost1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &cost2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &costBoth); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &need1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &need2); err != nil {
		log.Fatal(err)
	}

	return minimumCost(cost1, cost2, costBoth, need1, need2)
}

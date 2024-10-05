package problem134

import (
	"encoding/json"
	"log"
	"strings"
)

func canCompleteCircuit(gas []int, cost []int) int {

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

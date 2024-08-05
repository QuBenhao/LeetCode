package problem2398

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumRobots(chargeTimes []int, runningCosts []int, budget int64) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var chargeTimes []int
	var runningCosts []int
	var budget int64

	if err := json.Unmarshal([]byte(inputValues[0]), &chargeTimes); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &runningCosts); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &budget); err != nil {
		log.Fatal(err)
	}

	return maximumRobots(chargeTimes, runningCosts, budget)
}

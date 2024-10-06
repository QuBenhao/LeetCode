package problem871

import (
	"encoding/json"
	"log"
	"strings"
)

func minRefuelStops(target int, startFuel int, stations [][]int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var target int
	var startFuel int
	var stations [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &target); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &startFuel); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &stations); err != nil {
		log.Fatal(err)
	}

	return minRefuelStops(target, startFuel, stations)
}

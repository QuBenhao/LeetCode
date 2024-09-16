package problem815

import (
	"encoding/json"
	"log"
	"strings"
)

func numBusesToDestination(routes [][]int, source int, target int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var routes [][]int
	var source int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &routes); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &source); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &target); err != nil {
		log.Fatal(err)
	}

	return numBusesToDestination(routes, source, target)
}

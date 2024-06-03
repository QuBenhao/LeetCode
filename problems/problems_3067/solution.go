package problem3067

import (
	"encoding/json"
	"log"
	"strings"
)

func countPairsOfConnectableServers(edges [][]int, signalSpeed int) []int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var edges [][]int
	var signalSpeed int

	if err := json.Unmarshal([]byte(values[0]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &signalSpeed); err != nil {
		log.Fatal(err)
	}

	return countPairsOfConnectableServers(edges, signalSpeed)
}

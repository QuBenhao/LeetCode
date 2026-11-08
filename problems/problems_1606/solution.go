package problem1606

import (
	"encoding/json"
	"log"
	"strings"
)

func busiestServers(k int, arrival []int, load []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int
	var arrival []int
	var load []int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &arrival); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &load); err != nil {
		log.Fatal(err)
	}

	return busiestServers(k, arrival, load)
}

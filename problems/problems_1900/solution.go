package problem1900

import (
	"encoding/json"
	"log"
	"strings"
)

func earliestAndLatest(n int, firstPlayer int, secondPlayer int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var firstPlayer int
	var secondPlayer int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &firstPlayer); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &secondPlayer); err != nil {
		log.Fatal(err)
	}

	return earliestAndLatest(n, firstPlayer, secondPlayer)
}

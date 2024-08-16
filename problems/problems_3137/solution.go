package problem3137

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumOperationsToMakeKPeriodic(word string, k int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &word); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return minimumOperationsToMakeKPeriodic(word, k)
}

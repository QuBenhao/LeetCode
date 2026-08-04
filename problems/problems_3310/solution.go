package problem3310

import (
	"encoding/json"
	"log"
	"strings"
)

func remainingMethods(n int, k int, invocations [][]int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var k int
	var invocations [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &invocations); err != nil {
		log.Fatal(err)
	}

	return remainingMethods(n, k, invocations)
}

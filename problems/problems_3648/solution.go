package problem3648

import (
	"encoding/json"
	"log"
	"strings"
)

func minSensors(n int, m int, k int) int {
	k = 2*k + 1
	return ((m-1)/k + 1) * ((n-1)/k + 1)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var m int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return minSensors(n, m, k)
}

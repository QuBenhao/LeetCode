package problem3538

import (
	"encoding/json"
	"log"
	"strings"
)

func minTravelTime(l int, n int, k int, position []int, time []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var l int
	var n int
	var k int
	var position []int
	var time []int

	if err := json.Unmarshal([]byte(inputValues[0]), &l); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &position); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &time); err != nil {
		log.Fatal(err)
	}

	return minTravelTime(l, n, k, position, time)
}

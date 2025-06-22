package problem3594

import (
	"encoding/json"
	"log"
	"strings"
)

func minTime(n int, k int, m int, time []int, mul []float64) float64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var k int
	var m int
	var time []int
	var mul []float64

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &time); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &mul); err != nil {
		log.Fatal(err)
	}

	return minTime(n, k, m, time, mul)
}

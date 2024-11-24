package problem743

import (
	"encoding/json"
	"log"
	"strings"
)

func networkDelayTime(times [][]int, n int, k int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var times [][]int
	var n int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &times); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return networkDelayTime(times, n, k)
}

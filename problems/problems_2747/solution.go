package problem2747

import (
	"encoding/json"
	"log"
	"strings"
)

func countServers(n int, logs [][]int, x int, queries []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var logs [][]int
	var x int
	var queries []int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &logs); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &x); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &queries); err != nil {
		log.Fatal(err)
	}

	return countServers(n, logs, x, queries)
}

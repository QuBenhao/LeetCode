package problem3607

import (
	"encoding/json"
	"log"
	"strings"
)

func processQueries(c int, connections [][]int, queries [][]int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var c int
	var connections [][]int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &c); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &connections); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &queries); err != nil {
		log.Fatal(err)
	}

	return processQueries(c, connections, queries)
}

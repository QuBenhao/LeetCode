package problem2536

import (
	"encoding/json"
	"log"
	"strings"
)

func rangeAddQueries(n int, queries [][]int) [][]int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return rangeAddQueries(n, queries)
}

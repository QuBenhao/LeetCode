package problem3590

import (
	"encoding/json"
	"log"
	"strings"
)

func kthSmallest(par []int, vals []int, queries [][]int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var par []int
	var vals []int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &par); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &vals); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &queries); err != nil {
		log.Fatal(err)
	}

	return kthSmallest(par, vals, queries)
}

package problem3620

import (
	"encoding/json"
	"log"
	"strings"
)

func findMaxPathScore(edges [][]int, online []bool, k int64) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges [][]int
	var online []bool
	var k int64

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &online); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return findMaxPathScore(edges, online, k)
}

package problem3464

import (
	"encoding/json"
	"log"
	"strings"
)

func maxDistance(side int, points [][]int, k int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var side int
	var points [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &side); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &points); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return maxDistance(side, points, k)
}

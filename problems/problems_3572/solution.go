package problem3572

import (
	"encoding/json"
	"log"
	"strings"
)

func maxSumDistinctTriplet(x []int, y []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var x []int
	var y []int

	if err := json.Unmarshal([]byte(inputValues[0]), &x); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &y); err != nil {
		log.Fatal(err)
	}

	return maxSumDistinctTriplet(x, y)
}

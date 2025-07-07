package problem1751

import (
	"encoding/json"
	"log"
	"strings"
)

func maxValue(events [][]int, k int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var events [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &events); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maxValue(events, k)
}

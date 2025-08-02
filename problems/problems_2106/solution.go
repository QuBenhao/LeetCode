package problem2106

import (
	"encoding/json"
	"log"
	"strings"
)

func maxTotalFruits(fruits [][]int, startPos int, k int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var fruits [][]int
	var startPos int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &fruits); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &startPos); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return maxTotalFruits(fruits, startPos, k)
}

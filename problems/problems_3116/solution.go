package problem3116

import (
	"encoding/json"
	"log"
	"strings"
)

func findKthSmallest(coins []int, k int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var coins []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &coins); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return findKthSmallest(coins, k)
}

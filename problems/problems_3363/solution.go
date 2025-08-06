package problem3363

import (
	"encoding/json"
	"log"
	"strings"
)

func maxCollectedFruits(fruits [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var fruits [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &fruits); err != nil {
		log.Fatal(err)
	}

	return maxCollectedFruits(fruits)
}

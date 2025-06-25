package problem1802

import (
	"encoding/json"
	"log"
	"strings"
)

func maxValue(n int, index int, maxSum int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var index int
	var maxSum int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &index); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &maxSum); err != nil {
		log.Fatal(err)
	}

	return maxValue(n, index, maxSum)
}

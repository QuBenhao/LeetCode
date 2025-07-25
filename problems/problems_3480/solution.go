package problem3480

import (
	"encoding/json"
	"log"
	"strings"
)

func maxSubarrays(n int, conflictingPairs [][]int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var conflictingPairs [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &conflictingPairs); err != nil {
		log.Fatal(err)
	}

	return maxSubarrays(n, conflictingPairs)
}

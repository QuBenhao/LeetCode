package problem3693

import (
	"encoding/json"
	"log"
	"strings"
)

func climbStairs(n int, costs []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var costs []int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &costs); err != nil {
		log.Fatal(err)
	}

	return climbStairs(n, costs)
}

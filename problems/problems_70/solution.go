package problem70

import (
	"encoding/json"
	"log"
	"strings"
)

func climbStairs(n int) int {
	a, b := 1, 1
	for i := 0; i < n-1; i++ {
		a, b = b, a+b
	}
	return b
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return climbStairs(n)
}

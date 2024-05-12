package problem1553

import (
	"encoding/json"
	"log"
	"strings"
)

func minDays(n int) int {
	return 0
}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var n int

	if err := json.Unmarshal([]byte(values[0]), &n); err != nil {
		log.Fatal(err)
	}

	return minDays(n)
}

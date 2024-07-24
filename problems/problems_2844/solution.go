package problem2844

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumOperations(num string) int {
	n, zero := len(num), false
	for i, five := n-1, false; i >= 0; i-- {
		c := num[i]
		if zero && (c == '0' || c == '5') ||
			five && (c == '2' || c == '7') {
			return n - i - 2
		}
		if c == '0' {
			zero = true
		}
		if c == '5' {
			five = true
		}
	}
	if zero {
		return n - 1
	}
	return n
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num string

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return minimumOperations(num)
}

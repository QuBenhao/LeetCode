package problem3622

import (
	"encoding/json"
	"log"
	"strings"
)

func checkDivisibility(n int) bool {
	s, m := 0, 1
	for num := n; num > 0; num /= 10 {
		d := num % 10
		s += d
		m *= d
	}
	return n%(m+s) == 0
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return checkDivisibility(n)
}

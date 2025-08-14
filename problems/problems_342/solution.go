package problem342

import (
	"encoding/json"
	"log"
	"strings"
)

func isPowerOfFour(n int) bool {
	if n <= 0 || (n&(n-1)) != 0 {
		return false
	}
	return (n-1)%3 == 0
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return isPowerOfFour(n)
}

package problem779

import (
	"encoding/json"
	"log"
	"strings"
)

func kthGrammar(n int, k int) int {
	if n == 1 {
		return 0
	}
	parent := kthGrammar(n-1, (k+1)/2)
	return (1 - parent) ^ (k & 1)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return kthGrammar(n, k)
}

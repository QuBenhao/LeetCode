package problem2612

import (
	"encoding/json"
	"log"
	"strings"
)

func minReverseOperations(n int, p int, banned []int, k int) []int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var p int
	var banned []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &p); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &banned); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &k); err != nil {
		log.Fatal(err)
	}

	return minReverseOperations(n, p, banned, k)
}

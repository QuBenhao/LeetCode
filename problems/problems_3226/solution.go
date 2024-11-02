package problem3226

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

func minChanges(n int, k int) int {
	if (n & k) != k {
		return -1
	}
	return bits.OnesCount(uint(n ^ k))
}


func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return minChanges(n, k)
}

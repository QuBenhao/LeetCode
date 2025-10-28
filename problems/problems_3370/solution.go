package problem3370

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

func smallestNumber(n int) int {
	return 1<<bits.Len(uint(n)) - 1
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return smallestNumber(n)
}

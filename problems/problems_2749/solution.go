package problem2749

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

func makeTheIntegerZero(num1 int, num2 int) int {
	var x int64
	x = int64(num1)
	for k := 1; ; k++ {
		x -= int64(num2)
		if int64(k) > x {
			break
		}
		if bits.OnesCount64(uint64(x)) <= k {
			return k
		}
	}
	return -1
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num1 int
	var num2 int

	if err := json.Unmarshal([]byte(inputValues[0]), &num1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &num2); err != nil {
		log.Fatal(err)
	}

	return makeTheIntegerZero(num1, num2)
}

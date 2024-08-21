package problem3007

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

func findMaximumNumber(k int64, x int) int64 {
	num, preOne := int64(0), 0
	for i := bits.Len(uint((k+1)<<x)) - 1; i >= 0; i-- {
		if cur := int64(preOne<<i + i/x<<i>>1); cur <= k {
			k -= cur
			num |= 1 << i
			if (i+1)%x == 0 {
				preOne += 1
			}
		}
	}
	return num - 1
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int64
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &x); err != nil {
		log.Fatal(err)
	}

	return findMaximumNumber(k, x)
}

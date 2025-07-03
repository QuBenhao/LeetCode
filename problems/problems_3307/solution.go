package problem3307

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

func kthCharacter(k int64, operations []int) byte {
	count := 0
	for k > 1 {
		idx := 63 - bits.LeadingZeros64(uint64(k-1))
		if operations[idx] == 1 {
			count++
		}
		k -= 1 << idx
	}
	return byte('a' + count%26)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int64
	var operations []int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &operations); err != nil {
		log.Fatal(err)
	}

	return kthCharacter(k, operations)
}

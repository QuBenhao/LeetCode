package problem3304

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

func kthCharacter(k int) byte {
	count := 0
	for k > 1 {
		k -= 1 << (31 - bits.LeadingZeros32(uint32(k-1)))
		count++
	}
	return 'a' + byte(count%26)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}

	return kthCharacter(k)
}

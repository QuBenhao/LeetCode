package problem2275

import (
	"encoding/json"
	"log"
	"strings"
)

func largestCombination(candidates []int) (ans int) {
	bits := make([]int, 32)
	for _, v := range candidates {
		for i := 0; v > 0; i++ {
			bits[i] += v & 1
			ans = max(ans, bits[i])
			v >>= 1
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var candidates []int

	if err := json.Unmarshal([]byte(inputValues[0]), &candidates); err != nil {
		log.Fatal(err)
	}

	return largestCombination(candidates)
}

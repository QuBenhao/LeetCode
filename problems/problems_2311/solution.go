package problem2311

import (
	"encoding/json"
	"log"
	"strings"
)

func longestSubsequence(s string, k int) int {
	ans := strings.Count(s, "0")
	n, cur := len(s), 0
	for i := range min(n, 31) {
		if s[n-1-i] == '1' && (cur|(1<<i)) <= k {
			cur |= (1 << i)
			ans++
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return longestSubsequence(s, k)
}

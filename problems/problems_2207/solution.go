package problem2207

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumSubsequenceCount(text string, pattern string) (ans int64) {
	p0, p1 := int64(0), int64(0)
	r0, r1 := rune(pattern[0]), rune(pattern[1])
	for _, c := range text {
		if c == r1 {
			ans += p0
			p1++
		}
		if c == r0 {
			p0++
		}
	}
	ans += max(p0, p1)
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var text string
	var pattern string

	if err := json.Unmarshal([]byte(inputValues[0]), &text); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &pattern); err != nil {
		log.Fatal(err)
	}

	return maximumSubsequenceCount(text, pattern)
}

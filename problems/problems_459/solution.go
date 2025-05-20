package problem459

import (
	"encoding/json"
	"log"
	"strings"
)

func repeatedSubstringPattern(s string) bool {
	return strings.Index((s + s)[1:], s) != len(s)-1
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return repeatedSubstringPattern(s)
}

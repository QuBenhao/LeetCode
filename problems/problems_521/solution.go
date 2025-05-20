package problem521

import (
	"encoding/json"
	"log"
	"strings"
)

func findLUSlength(a string, b string) int {
	if a != b {
		return max(len(a), len(b))
	}
	return -1
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var a string
	var b string

	if err := json.Unmarshal([]byte(values[0]), &a); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &b); err != nil {
		log.Fatal(err)
	}

	return findLUSlength(a, b)
}

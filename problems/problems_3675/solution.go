package problem3675

import (
	"encoding/json"
	"log"
	"strings"
)

func minOperations(s string) int {
	cur := 26
	for _, r := range s {
		if r != 'a' {
			cur = min(cur, int(r)-'a')
		}
	}
	return 26 - cur
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return minOperations(s)
}

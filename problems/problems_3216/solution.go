package problem3216

import (
	"encoding/json"
	"log"
	"strings"
)

func getSmallestString(s string) string {
	n := len(s)
	for i := 0; i < n-1; i++ {
		if s[i] > s[i+1] && s[i]%2 == s[i+1]%2 {
			return s[:i] + string(s[i+1]) + string(s[i]) + s[i+2:]
		}
	}
	return s
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return getSmallestString(s)
}

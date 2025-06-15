package problem316

import (
	"encoding/json"
	"log"
	"strings"
)

func removeDuplicateLetters(s string) string {
	lastIndex := make([]int, 26)
	seen := make([]bool, 26)
	var result []byte
	for i, c := range s {
		lastIndex[c-'a'] = i
	}
	for i, c := range s {
		if seen[c-'a'] {
			continue
		}
		for len(result) > 0 && result[len(result)-1] > byte(c) && lastIndex[result[len(result)-1]-'a'] > i {
			seen[result[len(result)-1]-'a'] = false
			result = result[:len(result)-1]
		}
		result = append(result, byte(c))
		seen[c-'a'] = true
	}
	return string(result)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return removeDuplicateLetters(s)
}

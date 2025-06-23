package problem1704

import (
	"encoding/json"
	"log"
	"strings"
)

func halvesAreAlike(s string) bool {
	isVowel := func(c byte) bool {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
			c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'
	}
	n := len(s)
	count := 0
	for i := 0; i < n/2; i++ {
		if isVowel(s[i]) {
			count++
		}
		if isVowel(s[n-i-1]) {
			count--
		}
	}
	return count == 0
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return halvesAreAlike(s)
}

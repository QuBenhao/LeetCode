package problem3136

import (
	"encoding/json"
	"log"
	"strings"
)

func isValid(word string) bool {
	if len(word) < 3 {
		return false
	}
	var hasVowel, hasConsonant bool
	for _, c := range word {
		if c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' {
			lowerC := c | 0x20
			if lowerC == 'a' || lowerC == 'e' || lowerC == 'i' || lowerC == 'o' || lowerC == 'u' {
				hasVowel = true
			} else {
				hasConsonant = true
			}
		} else if c < '0' || c > '9' {
			return false // Invalid character
		}
	}
	return hasVowel && hasConsonant
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word string

	if err := json.Unmarshal([]byte(inputValues[0]), &word); err != nil {
		log.Fatal(err)
	}

	return isValid(word)
}

package problem520

import (
	"encoding/json"
	"log"
	"strings"
)

func detectCapitalUse(word string) bool {
	if word[len(word)-1] >= 'A' && word[len(word)-1] <= 'Z' {
		return strings.ToUpper(word) == word
	}
	if word[0] >= 'A' && word[0] <= 'Z' {
		return strings.ToLower(word[1:]) == word[1:]
	}
	return strings.ToLower(word) == word
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var word string

	if err := json.Unmarshal([]byte(values[0]), &word); err != nil {
		log.Fatal(err)
	}

	return detectCapitalUse(word)
}

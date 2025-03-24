package problem2255

import (
	"encoding/json"
	"log"
	"strings"
)

func countPrefixes(words []string, s string) (ans int) {
	for _, word := range words {
		if s[:len(word)] == word {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &s); err != nil {
		log.Fatal(err)
	}

	return countPrefixes(words, s)
}

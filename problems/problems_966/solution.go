package problem966

import (
	"encoding/json"
	"log"
	"strings"
)

func spellchecker(wordlist []string, queries []string) []string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var wordlist []string
	var queries []string

	if err := json.Unmarshal([]byte(inputValues[0]), &wordlist); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return spellchecker(wordlist, queries)
}

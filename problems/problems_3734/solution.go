package problem3734

import (
	"encoding/json"
	"log"
	"strings"
)

func lexPalindromicPermutation(s string, target string) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var target string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return lexPalindromicPermutation(s, target)
}

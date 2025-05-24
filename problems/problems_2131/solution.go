package problem2131

import (
	"encoding/json"
	"log"
	"strings"
)

func longestPalindrome(words []string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return longestPalindrome(words)
}

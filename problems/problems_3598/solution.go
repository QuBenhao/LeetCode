package problem3598

import (
	"encoding/json"
	"log"
	"strings"
)

func longestCommonPrefix(words []string) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return longestCommonPrefix(words)
}

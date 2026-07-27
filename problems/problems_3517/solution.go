package problem3517

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestPalindrome(s string) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return smallestPalindrome(s)
}

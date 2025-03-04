package problem1328

import (
	"encoding/json"
	"log"
	"strings"
)

func breakPalindrome(palindrome string) string {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var palindrome string

	if err := json.Unmarshal([]byte(inputValues[0]), &palindrome); err != nil {
		log.Fatal(err)
	}

	return breakPalindrome(palindrome)
}

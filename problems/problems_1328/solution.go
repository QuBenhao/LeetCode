package problem1328

import (
	"encoding/json"
	"log"
	"strings"
)

func breakPalindrome(palindrome string) string {
	n := len(palindrome)
	if n == 1 {
		return ""
	}
	mid := n / 2
	for i := range mid {
		if palindrome[i] != 'a' {
			return palindrome[:i] + "a" + palindrome[i+1:]
		}
	}
	return palindrome[:n-1] + "b"
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var palindrome string

	if err := json.Unmarshal([]byte(inputValues[0]), &palindrome); err != nil {
		log.Fatal(err)
	}

	return breakPalindrome(palindrome)
}

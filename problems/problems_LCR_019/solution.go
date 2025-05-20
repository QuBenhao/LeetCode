package problemLCR_019

import (
	"encoding/json"
	"log"
	"strings"
)

func isPalindrome(s string, left, right int) bool {
	for ; left < right; left++ {
		if s[left] != s[right] {
			return false
		}
		right--
	}
	return true
}

func validPalindrome(s string) bool {
	for left, right := 0, len(s)-1; left < right; left++ {
		if s[left] != s[right] {
			return isPalindrome(s, left+1, right) || isPalindrome(s, left, right-1)
		}
		right--
	}
	return true
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return validPalindrome(s)
}

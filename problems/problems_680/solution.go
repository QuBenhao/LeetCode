package problem680

import (
	"encoding/json"
	"log"
	"strings"
)

func validPalindrome(s string) bool {
	isPalindrome := func(str string, l, r int) bool {
		for l < r {
			if str[l] != str[r] {
				return false
			}
			l++
			r--
		}
		return true
	}
	for left, right := 0, len(s)-1; left < right; left++ {
		if s[left] != s[right] {
			return isPalindrome(s, left+1, right) || isPalindrome(s, left, right-1)
		}
		right--
	}
	return true
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return validPalindrome(s)
}

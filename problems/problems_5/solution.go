package problem5

import (
	"encoding/json"
	"log"
	"strings"
)

func longestPalindrome(s string) string {
	if len(s) == 0 {
		return s
	}
	start, end := 0, 0
	for i := 0; i < len(s); i++ {
		left, right := i, i
		for left >= 0 && right < len(s) && s[left] == s[right] {
			left--
			right++
		}
		if right-left-2 > end-start {
			start = left + 1
			end = right - 1
		}
		left, right = i, i+1
		for left >= 0 && right < len(s) && s[left] == s[right] {
			left--
			right++
		}
		if right-left-2 > end-start {
			start = left + 1
			end = right - 1
		}
	}
	return s[start : end+1]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return longestPalindrome(s)
}

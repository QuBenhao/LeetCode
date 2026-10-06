package problem2663

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestBeautifulString(S string, k int) string {
	limit := 'a' + byte(k)
	s := []byte(S)
	n := len(s)
	i := n - 1 // Start with the last letter
	s[i]++     // Increment first
	for i < n {
		if s[i] == limit { // A carry is needed
			if i == 0 { // Cannot carry
				return ""
			}
			// Carry
			s[i] = 'a'
			i--
			s[i]++
		} else if i > 0 && s[i] == s[i-1] || i > 1 && s[i] == s[i-2] {
			s[i]++ // If s[i] forms a palindrome with characters to its left, keep incrementing s[i]
		} else {
			i++ // Move forward to check for palindromes in the suffix
		}
	}
	return string(s)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string
	var k int

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return smallestBeautifulString(s, k)
}

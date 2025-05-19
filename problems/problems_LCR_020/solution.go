package problemLCR_020

import (
	"encoding/json"
	"log"
	"strings"
)

func countSubstrings(s string) (ans int) {
	n := len(s)
	isPalindrome := make([][]bool, n)
	for i := range n {
		isPalindrome[i] = make([]bool, n)
		isPalindrome[i][i] = true
		ans++
	}
	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			if s[i] == s[j] && (j-i < 3 || isPalindrome[i+1][j-1]) {
				ans++
				isPalindrome[i][j] = true
			}
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return countSubstrings(s)
}

package problemLCR_086

import (
	"encoding/json"
	"log"
	"strings"
)

func partition(s string) (ans [][]string) {
	n := len(s)
	isPalindrome := make([][]bool, n)
	for i := range isPalindrome {
		isPalindrome[i] = make([]bool, n)
		isPalindrome[i][i] = true
	}
	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			isPalindrome[i][j] = (s[i] == s[j]) && (j-i < 3 || isPalindrome[i+1][j-1])
		}
	}
	var path []string
	var backtrack func(int)
	backtrack = func(start int) {
		if start == n {
			ans = append(ans, append([]string{}, path...))
			return
		}
		for right := start; right < n; right++ {
			if isPalindrome[start][right] {
				path = append(path, s[start:right+1])
				backtrack(right + 1)
				path = path[:len(path)-1]
			}
		}
	}
	backtrack(0)
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return partition(s)
}

package problem1745

import (
	"encoding/json"
	"log"
	"strings"
)

func checkPartitioning(s string) bool {
	n := len(s)
	isPalindrome := make([][]bool, n)
	for i := range isPalindrome {
		isPalindrome[i] = make([]bool, n)
		isPalindrome[i][i] = true
	}
	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			isPalindrome[i][j] = s[i] == s[j] && (i+2 >= j || isPalindrome[i+1][j-1])
		}
	}
	var left, right []int
	for i := range n {
		if isPalindrome[0][i] {
			left = append(left, i)
		}
		if isPalindrome[i][n-1] {
			right = append(right, i)
		}
	}
	for _, l := range left {
		for _, r := range right {
			if r <= l+1 {
				continue
			}
			if isPalindrome[l+1][r-1] {
				return true
			}
		}
	}
	return false
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return checkPartitioning(s)
}

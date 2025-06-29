package problem3598

import (
	"encoding/json"
	"log"
	"strings"
)

func getPrefixLen(words []string, i, j int) (k int) {
	for k = 0; k < len(words[i]) && k < len(words[j]) && words[i][k] == words[j][k]; k++ {
	}
	return
}

func longestCommonPrefix(words []string) []int {
	n := len(words)
	if n == 1 {
		return []int{0}
	}
	lcp := make([]int, n)
	for i := range n - 1 {
		lcp[i+1] = getPrefixLen(words, i, i+1)
	}
	suffix := make([]int, n)
	for i := n - 2; i >= 0; i-- {
		suffix[i] = max(suffix[i+1], lcp[i+1])
	}
	ans := make([]int, n)
	ans[0] = suffix[1]
	prefix := 0
	for i := 1; i < n-1; i++ {
		ans[i] = max(max(prefix, suffix[i+1]), getPrefixLen(words, i-1, i+1))
		prefix = max(prefix, lcp[i])
	}
	ans[n-1] = prefix
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return longestCommonPrefix(words)
}

package problem22

import (
	"encoding/json"
	"log"
	"strings"
)

func generateParenthesis(n int) (ans []string) {
	var backtrack func(path []byte, left, right int)
	backtrack = func(path []byte, left, right int) {
		if left == n && right == n {
			ans = append(ans, string(path))
			return
		}
		if left < n {
			path = append(path, '(')
			backtrack(path, left+1, right)
			path = path[:len(path)-1]
		}
		if right < left {
			path = append(path, ')')
			backtrack(path, left, right+1)
			path = path[:len(path)-1]
		}
	}
	backtrack([]byte{}, 0, 0)
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return generateParenthesis(n)
}

package problem32

import (
	"encoding/json"
	"log"
	"strings"
)

func longestValidParentheses(s string) (ans int) {
	st := []int{}
	for i, c := range s {
		if c == '(' {
			st = append(st, i)
		} else {
			if len(st) > 0 && s[st[len(st)-1]] == '(' {
				st = st[:len(st)-1]
				if len(st) == 0 {
					ans = max(ans, i+1)
				} else {
					ans = max(ans, i-st[len(st)-1])
				}
			} else {
				st = append(st, i)
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

	return longestValidParentheses(s)
}

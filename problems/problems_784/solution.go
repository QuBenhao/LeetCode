package problem784

import (
	"encoding/json"
	"log"
	"strings"
)

func letterCasePermutation(s string) (ans []string) {
	var dfs func(string, int)
	dfs = func(current string, index int) {
		if index == len(s) {
			ans = append(ans, current)
			return
		}
		dfs(current+string(s[index]), index+1)
		if s[index] < '0' || s[index] > '9' {
			dfs(current+string(s[index]^32), index+1)
		}
	}
	dfs("", 0)
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return letterCasePermutation(s)
}

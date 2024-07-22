package problem17

import (
	"encoding/json"
	"log"
	"strings"
)

func letterCombinations(digits string) (ans []string) {
	if len(digits) == 0 {
		return
	}
	translator := map[rune][]string{
		'2': {"a", "b", "c"},
		'3': {"d", "e", "f"},
		'4': {"g", "h", "i"},
		'5': {"j", "k", "l"},
		'6': {"m", "n", "o"},
		'7': {"p", "q", "r", "s"},
		'8': {"t", "u", "v"},
		'9': {"w", "x", "y", "z"},
	}
	var dfs func(int, string)
	dfs = func(i int, s string) {
		if i == len(digits) {
			ans = append(ans, s)
			return
		}
		for _, c := range translator[rune(digits[i])] {
			dfs(i+1, s+c)
		}
	}
	dfs(0, "")
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var digits string

	if err := json.Unmarshal([]byte(inputValues[0]), &digits); err != nil {
		log.Fatal(err)
	}

	return letterCombinations(digits)
}

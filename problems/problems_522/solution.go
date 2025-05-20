package problem522

import (
	"encoding/json"
	"log"
	"strings"
)

func findLUSlength(strs []string) int {
	ans := -1
out:
	for i, s := range strs {
		if len(s) > ans {
			for j, s_ := range strs {
				if j != i && isSubStr(s, s_) {
					continue out
				}
			}
			ans = len(s)
		}
	}
	return ans
}

func isSubStr(s1, s2 string) bool {
	m, n := len(s1), len(s2)
	if m > n {
		return false
	}
	i := 0
	for j := 0; i < m && j < n; j++ {
		if s1[i] == s2[j] {
			i++
		}
	}
	return i == m
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var strs []string

	if err := json.Unmarshal([]byte(values[0]), &strs); err != nil {
		log.Fatal(err)
	}

	return findLUSlength(strs)
}

package problem3

import (
	"encoding/json"
	"log"
	"strings"
)

func lengthOfLongestSubstring(s string) (ans int) {
	mp, j := map[rune]int{}, -1
	for i, v := range s {
		if idx, ok := mp[v]; ok {
			j = max(j, idx)
		}
		ans = max(ans, i-j)
		mp[v] = i
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return lengthOfLongestSubstring(s)
}

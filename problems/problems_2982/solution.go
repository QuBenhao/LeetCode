package problem2982

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func maximumLength(s string) int {
	groups := [26][]int{}
	count := 0
	for i := range s {
		count++
		if i == len(s)-1 || s[i] != s[i+1] {
			groups[s[i]-'a'] = append(groups[s[i]-'a'], count)
			count = 0
		}
	}
	ans := 0
	for _, a := range groups {
		if len(a) == 0 {
			continue
		}
		slices.SortFunc(a, func(a, b int) int { return b - a })
		a = append(a, 0, 0)
		ans = max(ans, a[0]-2, min(a[0]-1, a[1]), a[2])
	}
	if ans == 0 {
		return -1
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return maximumLength(s)
}

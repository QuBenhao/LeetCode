package problem2414

import (
	"encoding/json"
	"log"
	"strings"
)

func longestContinuousSubstring(s string) int {
	ans := 1
	for i, cur := 0, 1; i < len(s)-1; i++ {
		if s[i+1]-s[i] == 1 {
			cur++
			ans = max(ans, cur)
		} else {
			cur = 1
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return longestContinuousSubstring(s)
}

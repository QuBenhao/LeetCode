package problemLCR_092

import (
	"encoding/json"
	"log"
	"strings"
)

func minFlipsMonoIncr(s string) int {
	n := len(s)
	one, ans := 0, n
	for i := 0; i < n; i++ {
		ans = min(ans, one*2-i)
		one += int(s[i] - '0')
	}
	return min(one, ans+n-one)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return minFlipsMonoIncr(s)
}

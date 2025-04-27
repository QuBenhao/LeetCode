package problem1456

import (
	"encoding/json"
	"log"
	"strings"
)

func maxVowels(s string, k int) (ans int) {
	isVowels := func(b byte) int {
		if b == 'a' || b == 'e' || b == 'i' || b == 'o' || b == 'u' {
			return 1
		}
		return 0
	}
	window, n := 0, len(s)
	for i := 0; i < n; i++ {
		window += isVowels(s[i])
		if i >= k {
			window -= isVowels(s[i-k])
		}
		ans = max(ans, window)
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maxVowels(s, k)
}

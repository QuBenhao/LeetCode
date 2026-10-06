package problem1542

import (
	"encoding/json"
	"log"
	"strings"
)

func longestAwesome(s string) (ans int) {
	const D = 10 // Number of possible distinct characters in s
	n := len(s)
	pos := [1 << D]int{}
	for i := range pos {
		pos[i] = n // n means this prefix XOR has not been found
	}
	pos[0] = -1 // pre[-1] = 0
	pre := 0
	for i, c := range s {
		pre ^= 1 << (c - '0')
		for d := 0; d < D; d++ {
			ans = max(ans, i-pos[pre^(1<<d)]) // Odd count
		}
		ans = max(ans, i-pos[pre]) // Even count
		if pos[pre] == n {         // Record index i on the first occurrence of prefix XOR pre
			pos[pre] = i
		}
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return longestAwesome(s)
}

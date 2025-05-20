package problem2734

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestString(s string) string {
	var ans []byte
	left := 0
	for left < len(s) && s[left] == 'a' {
		ans = append(ans, s[left])
		left++
	}
	if left == len(s) {
		ans = ans[:len(ans)-1]
		ans = append(ans, 'z')
		return string(ans)
	}
	right := left
	for right < len(s) && s[right] != 'a' {
		ans = append(ans, s[right]-1)
		right++
	}
	return string(ans) + s[right:]
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return smallestString(s)
}

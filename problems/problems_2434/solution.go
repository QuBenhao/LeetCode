package problem2434

import (
	"encoding/json"
	"log"
	"strings"
)

func robotWithString(s string) string {
	n := len(s)
	suf := make([]byte, n+1)
	for i := range n + 1 {
		suf[i] = 'z'
	}
	for i := n - 1; i >= 0; i-- {
		suf[i] = min(suf[i+1], s[i])
	}
	var ans []byte
	var st []byte
	for i, c := range s {
		st = append(st, byte(c))
		for len(st) > 0 && st[len(st)-1] <= suf[i+1] {
			ans = append(ans, st[len(st)-1])
			st = st[:len(st)-1]
		}
	}
	return string(ans)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return robotWithString(s)
}

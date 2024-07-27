package problem3106

import (
	"encoding/json"
	"log"
	"strings"
)

func getSmallestString(s string, k int) string {
	distance := func(a, b byte) int {
		return int(min((b-a+26)%26, (a-b+26)%26))
	}
	var ans []byte
	idx := 0
	for idx < len(s) && k > 0 {
		if s[idx] == 'a' {
			ans = append(ans, s[idx])
			idx++
			continue
		}
		d := distance('a', s[idx])
		if k >= d {
			ans = append(ans, 'a')
			k -= d
		} else {
			ans = append(ans, s[idx]-byte(k))
			k = 0
		}
		idx++
	}
	return string(ans) + s[idx:]
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

	return getSmallestString(s, k)
}
